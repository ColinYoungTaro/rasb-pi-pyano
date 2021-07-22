
from control import HardWareController
from camera_dialog import CameraDialog, Dialog
from subWidget import Ui_Dialog
from service import BlockAnimationService, BlockState, MusicItemService, NoteBlock, PlayerService
from note import Music, Note
from GlobalConfig import GlobalConfig, MusicConfig
import sys
import typing
from PyQt5 import QtGui
import PyQt5
from PyQt5.QtCore import QRect, QTime, QTimer, Qt
from PyQt5.QtGui import QColor, QFont, QLinearGradient, QPaintEvent, QPainter, QPen, QPixmap

from PyQt5.QtWidgets import QAbstractItemView, QApplication, QDialog, QLabel,QListWidgetItem , QMainWindow, QProgressBar, QScroller, QWidget
from pyanoUI import Ui_Form as Window
import rsc
# Piano Label 

# 画钢琴的
class PianoCanvas(QLabel):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.pressed_key = [False] * 21

    def press(self,abs_note):
        self.pressed_key[abs_note-1] = True

    def release(self,abs_note):
        self.pressed_key[abs_note-1] = False

    def release_all(self):
        self.pressed_key = [False] * 21 


    def paintEvent(self, arg__1: PyQt5.QtGui.QPaintEvent) -> None:
        super().paintEvent(arg__1)
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QColor(0x202020))
        painter.drawRect(0,0,700,100)
        # painter.setPen(None)
        for i in range(21):
            white_board = QRect(5+i*33,0,30,100)
            line = QLinearGradient(white_board.topLeft(),white_board.bottomRight())
            if not self.pressed_key[i]:
                line.setColorAt(0,Qt.white)
                line.setColorAt(0.6,Qt.white)
                line.setColorAt(1,Qt.lightGray)
            else:
                line.setColorAt(0,Qt.lightGray)
                line.setColorAt(0.6,Qt.lightGray)
                line.setColorAt(1,Qt.gray)

            painter.setBrush(line)
            painter.drawRect(white_board)
        
        painter.setBrush(Qt.black)
        for i in range(21):
            id = i % 7
            if id == 2 or id == 6:
                continue
            painter.drawRect(26 +i*33,0,20,66)
        painter.end() 


class AnimationCanvas(QLabel):
    def __init__(self,parent: typing.Optional[PyQt5.QtWidgets.QWidget] = None) -> None:
        super().__init__(parent)
        self.setGeometry(0,0,700,500)
        self.current_time = 0


        self.frame_timer = QTimer()
        self.frame_timer.setInterval(GlobalConfig.dt)
        self.frame_timer.timeout.connect(self.on_frame_update)
        self.is_playing = True

        self.buffer_pixmap = QPixmap(700,500)
        self.buffer_pixmap.fill(Qt.transparent)

        self.service = BlockAnimationService()
        self.blocks = []
        self.piano = None

        self.related_progress_bar = None

    def bind_progress_bar(self, bar : QProgressBar):
        self.related_progress_bar = bar

    def bind_piano_canvas(self, piano : PianoCanvas):
        self.piano = piano

    def load_song(self,song_name):
        notes = Note.music_read(song_name)
        blocks = self.service.create_blocks(notes)
        self.blocks = blocks
        self.service.set_progress(0)
        self.service.on_init()

    def pause(self):
        self.frame_timer.stop()

    def start(self):
        self.frame_timer.start()

    def update_blocks_position(self,blocks):
        for index,block in enumerate(blocks):
            block : NoteBlock
            block.moveTop(int(block.y() + GlobalConfig.drop_speed_pixels_per_frame()))
            if block.state == BlockState.FLOAT:
                if block.bottom() > 400:
                    block.state = BlockState.TOUCHING
                    self.service.on_note_rect_touch(block)
                    if self.piano:
                        self.piano.press(block.note.abs_int_note)
                        self.piano.update()
                    if self.related_progress_bar:
                        self.related_progress_bar.setValue(self.service.get_progress())

            elif block.state == BlockState.TOUCHING:
                if block.top() > 400:
                    block.state = BlockState.LEFT
                    self.service.on_note_rect_leave(block)
                    if self.piano:
                        self.piano.release(block.note.abs_int_note)
                        self.piano.update()
                    
    def on_frame_update(self):
        self.update_blocks_position(self.blocks)
        self.update()
        self.frame_timer.start()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        buffer_painter = QPainter()
        self.buffer_pixmap.fill(Qt.transparent)
        buffer_painter.begin(self.buffer_pixmap)
        # 绘制钢琴键
        buffer_painter.setBrush(QColor(0x16825d))
        buffer_painter.setPen(QColor(0x16825d))
        for block in self.blocks:
            if self.service.rect_in_sight(block):
                buffer_painter.drawRect(block)
        buffer_painter.end()
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.buffer_pixmap)

# Window是QtDesigner设计的window
# 自己添加的部分组件 通过继承Window来实现
class UIWindow(Window):
    def __init__(self) -> None:
        super().__init__()
        self.item_clicked_listener = None
        self.player_service = PlayerService()
        self.dialog = None

    # 初始化样式和基本逻辑功能
    def init_components(self):

        self.animation_content = AnimationCanvas(self.frame)
        self.animation_content.bind_progress_bar(self.progressBar)
        self.piano_canvas = PianoCanvas(self.frame)
        self.piano_canvas.setGeometry(0,400,700,100)
        self.animation_content.bind_piano_canvas(self.piano_canvas)
        list_widget = self.listWidget
        QScroller.grabGesture(list_widget,QScroller.LeftMouseButtonGesture)
        list_widget.itemClicked.connect(self.on_item_clicked)
        list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        list_widget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        

        self.nextButton.clicked.connect(self.on_next_clicked)
        self.prevButton.clicked.connect(self.on_prev_clicked)
        self.playButton.clicked.connect(self.on_play_clicked)
        self.uploadButton.clicked.connect(self.on_upload_clicked)
        self.refresh_song_list()
        self.songLabel.setText("")

        self.button_style_pause()

        self.minusButton.clicked.connect(self.on_sub_button_clicked)
        self.addButton.clicked.connect(self.on_add_button_clicked)
        self.baseLabel.setAlignment(Qt.AlignCenter)

    def on_add_button_clicked(self):
        HardWareController.add_base()
        self.baseLabel.setText(str(HardWareController.base))

    def on_sub_button_clicked(self):
        HardWareController.minus_base()
        self.baseLabel.setText(str(HardWareController.base))

    def refresh_song_list(self):
        list_widget = self.listWidget
        list_widget.clear()
        list_widget.addItems(self.player_service.get_song_list())

    def button_style_pause(self):
        self.playButton.setStyleSheet('''
            #playButton{
                background-color:transparent;
                background-image:url(:/assets/pause_idle.png);
                outline:0px;
            }
            #playButton:pressed{
                background-color:transparent;
                background-image:url(:/assets/pause_selected.png);
                outline:0px;
            }
            ''') 
    def button_style_play(self):
        self.playButton.setStyleSheet('''
            #playButton{
                background-color:transparent;
                background-image:url(:/assets/play_idle.png);
                outline:0px;
            }
            #playButton:pressed{
                background-color:transparent;
                background-image:url(:/assets/play_selected.png);
                outline:0px;
            }
            ''')  



    # selected interface 
    def on_item_clicked(self,item:QListWidgetItem):
        self.player_service.select_song(item.text())
        self.piano_canvas.release_all()
        self.on_load_song(item.text())
        if self.item_clicked_listener is not None:
            self.item_clicked_listener(item)

    def on_load_song(self,name):
        self.animation_content.load_song(name)
        self.songLabel.setText(name)
        self.on_play()

    def set_item_clicked_listener(self,func):
        self.item_clicked_listener = func

    def on_next_clicked(self):
        self.player_service.on_next() 
        self.on_load_song(self.player_service.get_current_song())

    def on_prev_clicked(self):
        self.player_service.on_prev()
        self.on_load_song(self.player_service.get_current_song())

    def on_upload_clicked(self):
        self.dialog = CameraDialog()
        self.dialog.set_load_listener(self.refresh_song_list)


    def on_play(self):
        self.button_style_play()
        self.animation_content.start()
        self.player_service.on_play()
        self.player_service.set_play_state(True)

    def on_pause(self):
        self.button_style_pause()
        self.animation_content.pause()
        self.player_service.on_pause()
        self.player_service.set_play_state(False)


    def on_play_clicked(self):
        # print(self.player_service.get_current_song())
        if self.player_service.get_current_song():
            state = self.player_service.get_play_state()
            if state:
                self.on_pause()
            else:
                self.on_play()

            
        




# 单独分离UI层和事件层
# 事后这个类就被忘记了。。。
class UIWidget(QWidget):
    def __init__(self):
        super(UIWidget,self).__init__()
        self.ui = UIWindow()
        self.ui.setupUi(self)
        self.ui.init_components()
        self.ui.set_item_clicked_listener(self.on_item_clicked)
        


    def on_item_clicked(self,item:QListWidgetItem):
        pass 
        #dialog = CameraDialog()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        HardWareController.dispose()
        return super().closeEvent(a0)



