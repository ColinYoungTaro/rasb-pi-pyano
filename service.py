from control import HardWareController
from PyQt5.QtWidgets import QProgressBar, QPushButton
from note import Music, Note
from PyQt5.QtCore import QProcess, QRect, QThread
from GlobalConfig import GlobalConfig, MusicConfig
import os
import cv2
from predictor import Predictor

class BlockState:
    FLOAT = 0
    TOUCHING = 1
    LEFT = 2

class IO_STATE:
    PRESS = 1
    RELEASE = 0

class HardwareThread(QThread):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        while True:
            self.msleep(30)

    def press_note(self,note:Note):
        HardWareController.note_press(note)

    def release_note(self,note:Note):
        HardWareController.note_release(note)
        self.msleep(MusicConfig.get_unit_interval_second() * 500)
        HardWareController.note_idle(note)
            

class NoteBlock(QRect):
    def __init__(self,*args, **kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.state = BlockState.FLOAT
        self.note = None
    def set_note(self,note):
        self.note = note

class BlockAnimationService:
    def __init__(self) -> None:
        self.progress = 0
        self.blocks = []
        self.hardware_thread = HardwareThread()
        self.hardware_thread.start()
    
    def create_blocks(self,notes):
        self.blocks = []
        unit_ptr = 0
        for note in notes:
            note : Note
            if note.abs_int_note == -1:
                continue
            index = note.abs_int_note - 1
            note_pixel = note.duration * GlobalConfig.unit_height
            if index < 0: 
                unit_ptr += note_pixel
                continue
            y = -note_pixel - unit_ptr
            block = NoteBlock(5 + index * 33,y,33,note_pixel)
            block.set_note(note)
            self.blocks.append(block)
            unit_ptr += note_pixel + 0.5 * GlobalConfig.interval()

        return self.blocks

    def set_progress(self,i):
        self.progress = i

    def rect_in_sight(self,rect:QRect):
        return not (rect.y() > 400 or rect.y() + rect.height() < 0)

    def get_progress(self):
        return  int(100 * self.progress / len(self.blocks))

    def on_note_rect_touch(self,blk:NoteBlock):
        print(f"{blk.note} 按下")
        self.progress += 1
        self.hardware_thread.press_note(blk.note)
        
    def on_note_rect_leave(self,blk:NoteBlock):
        print(f"{blk.note} 抬起")
        self.hardware_thread.release_note(blk.note)


    def on_init(self):
        pass 


class MusicItemService:
    def __init__(self) -> None:
        pass

    def chord_list(self):
        fileList = os.listdir(MusicConfig.prefix)
        return fileList





class PlayerService:
    def __init__(self):
        self.is_playing = False
        self.current_song = None 
        self.song_list = os.listdir(MusicConfig.prefix)
        self.id_hash = {}
        for i,s in enumerate(self.song_list):
            self.id_hash[s] = i

        self.song_ptr = -1

    def get_song_list(self):
        self.song_list = os.listdir(MusicConfig.prefix)
        return os.listdir(MusicConfig.prefix)

    def get_play_state(self):
        return self.is_playing

    def set_play_state(self,b):
        self.is_playing = b

    def select_song(self,song_name):
        self.song_ptr = self.id_hash[song_name]

    def get_current_song(self):
        return None if self.song_ptr == -1 else self.song_list[self.song_ptr]

    def load_song(self):
        pass 

    def on_play(self):
        pass 

    def on_pause(self):
        pass

    def on_next(self):
        if len(self.song_list) > 0:
            self.song_ptr = (self.song_ptr + 1) % len(self.song_list)

    def on_prev(self):
        if len(self.song_list) > 0:
            self.song_ptr = (self.song_ptr - 1 + len(self.song_list)) % len(self.song_list)

class CameraService:
    def __init__(self) -> None:
        pass

    def on_load(self,name,img):
        # 在这里识别
        img = cv2.resize(img,(1280,720))
        pd = Predictor()
        
        cv2.imwrite('./cache/img.png',img)
        try:
            note,pitch,dur = pd.predict("./cache/img.png", "", "", 0.43, 0, 100)
        except ValueError:
            return -1 # 错误码

        notes = Note.convert_from_predicted_list(note,pitch,dur)
        Note.music_save(name,notes)
        return 0
        