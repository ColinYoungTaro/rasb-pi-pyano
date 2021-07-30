
from predictor import Predictor
from service import CameraService, PlayerService, PredictorServiceInstance
from PyQt5 import QtCore, QtGui
import PyQt5
from PyQt5.QtWidgets import QDialog
from subWidget import Ui_Dialog as SubDialog
import cv2

class Dialog(SubDialog):
    def __init__(self) -> None:
        super().__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.labelTip.setText("")

    def error_msg(self,msg):
        self.labelTip.setText(f'''<html><head/><body><p><span style=" color:#ff4564;">{msg}</span></p></body></html>''')

    def success_msg(self,msg):
        self.labelTip.setText(f'''<html><head/><body><p><span style=" color:#ffffff;">{msg}</span></p></body></html>''')


# QDialog
class CameraDialog(QDialog):

    def __init__(self,parent=None) -> None:
        super().__init__()
        self.ui = Dialog()
        self.ui.setupUi(self)
        self.load_listener = None 
        self.parent = parent
        self.init_components()
        self.init_threads()

        self.exec_()

    def init_threads(self):
        self.upload_thread = UploadThread()
        self.camera_thread = CameraInitThread()
        self.camera_thread.ready_signal.connect(self.on_camera_signal)
        self.upload_thread.ready_signal.connect(self.on_upload_signal)
        self.camera_thread.start()

    def init_components(self):
        self.ui.load_button.setVisible(False)
        self.ui.buttonOk.clicked.connect(self.on_ok_clicked)
        self.ui.buttonCancel.clicked.connect(self.on_cancel_clicked)
        self.ui.load_button.clicked.connect(self.on_load_clicked)
        self.ui.image.setText('''<html><head/><body><p><span style=" color:#ffffff; font-size:20px; font-family:等线 ">摄像机准备中，请稍后...</span></p></body></html>''')
        self.ui.image.setAlignment(QtCore.Qt.AlignCenter)
        self.ready = False
        # .camera_vc = None 
        
    def on_load_clicked(self):
        name:str = self.ui.inputName.text()
        if name == '':
            self.ui.error_msg("请输入文件名")
        else:
            self.upload_thread.set_img(self.cvimg)
            self.upload_thread.set_name(name)
            self.upload_thread.start()
            self.ui.success_msg("识别中，请稍后...")
        # UploadThread(self.cvimg)# .start()

    def on_ok_clicked(self):
        if self.ready:
            self.camera_thread.click()
            self.ui.load_button.setVisible(not self.camera_thread.is_running)
            self.ui.buttonOk.setText("确定" if self.camera_thread.is_running else "重拍") 
        #self.frame_timer.stop()

    

    def on_cancel_clicked(self):
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.camera_thread.exit()
        self.accept()


    def on_camera_signal(self,info):
        
        if info == 'ready':
            self.ready = True
            # self.camera_vc = self.camera_thread.vc
            
        elif info == 'capture':   
            self.cvimg = self.camera_thread.get_img()
            self.qimg = self.cvimg_to_qtimg(self.cvimg)
            pixmap = QtGui.QPixmap.fromImage(self.qimg)
            pixmap = pixmap.scaled(600, 330, QtCore.Qt.KeepAspectRatio)
            self.ui.image.setPixmap(pixmap)

    def on_upload_signal(self,info):
        if info == 'finished':
            if self.parent is not None and hasattr(self.parent,'refresh_song_list'):
                self.parent.refresh_song_list()
            # self.on_cancel_clicked()
            self.ui.success_msg("识别完成")

        elif info == 'failed':
            self.ui.error_msg("找不到简谱，请重新拍照")
    
    def cvimg_to_qtimg(self,cvimg)->QtGui.QImage:

        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QtGui.QImage(cvimg.data, width, height, width * depth, QtGui.QImage.Format_RGB888)

        return cvimg

    def set_load_listener(self,listener):
        self.load_listener = listener


class CameraInitThread(QtCore.QThread):

    ready_signal = QtCore.pyqtSignal(str)

    def __init__(self) -> None:
        super(CameraInitThread,self).__init__()
        self.vc = None
        self.img = None 
        self.is_running = True
        self.video_running = True

    def run(self):
        self.vc = cv2.VideoCapture(-1)
        
        print("ready")
        self.ready_signal.emit("ready")
        while self.video_running:
            if self.is_running:
                rval, frame = self.vc.read()
                self.img = frame
                self.ready_signal.emit("capture")
                self.msleep(100)

    def get_img(self):
        return self.img

    def click(self):
        self.is_running = not self.is_running

    def exit(self):
        self.vc.release()
        self.video_running = False


class UploadThread(QtCore.QThread):
    ready_signal = QtCore.pyqtSignal(str)
    def __init__(self) -> None:
        super(UploadThread,self).__init__()
        self.upload_service = CameraService()
        # self.upload_service.init_pd()
        self.name = ""

    def set_name(self,name):
        self.name = name 

    def set_img(self,img):
        self.img = img

    def run(self):
        status_code = self.upload_service.on_load(self.name,self.img)
        if status_code == -1:
            self.ready_signal.emit("failed")
        else:
            self.ready_signal.emit("finished")
            

        

        
