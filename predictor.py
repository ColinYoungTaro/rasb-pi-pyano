from tensorflow import keras
from data_preprocessor import Data_preprocessor
from data_reader import Data_reader
import numpy as np
import os
# from midiutil.MidiFile import MIDIFile
# import RPi.GPIO as GPIO
import time

class Predictor(object):
    """docstring for Predictor"""
    def __init__(self):
        # 加载识别模型
        self.model_note = keras.models.load_model("model/note.h5".encode("utf-8").decode("utf-8"))
        self.model_pitch = keras.models.load_model("model/pitch.h5")
        self.model_duration = keras.models.load_model("model/duration.h5")
        self.dp = Data_preprocessor()
        # self.dr = Data_reader()
        return

    def load_data(self, path, contrast_rate, line_rate):
        res = self.dp.data_preprocess(self.dp.load_img(path), contrast_rate, line_rate) #
        print(len(res))
        data = np.zeros((len(res), 40, 40, 3))
        for i in range(len(res)):
            data[i] = self.dp.constrain_img_size(res[i])
        return data

 
    def predict(self, path, path_save, file_name="new", contrast_rate=0.5, line_rate=0.2, tempo=80):
        data = self.load_data(path, contrast_rate, line_rate)
        print(data.shape)
        if len(data.shape) < 4:
            data.reshape((1, 40, 40, 3))
        y_note = np.argmax(self.model_note.predict(data), 1)
        y_pitch = np.argmax(self.model_pitch.predict(data), 1)
        y_duration = np.argmax(self.model_duration.predict(data), 1)
        
        result = self.generate_result(y_note, y_pitch, y_duration)
        
        #self.generate_midi(y_note, y_pitch, y_duration, tempo)
        #self.play(y_note,y_pitch,y_duration,tempo)

        file = open(path_save + file_name + '.sht', 'w')
        file.write("D 4 4 144\n")
        file.write(result)
        file.close()
        
        return(y_note,y_pitch,y_duration)

    def generate_result(self, note, pitch, duration):
        res = ""
        for i in range(len(note)):
            #print(note[i],duration[i],pitch[i])
            res += self.parse_note(note[i])
            if note[i] < 8:
                res += self.parse_pitch(pitch[i])
            res += self.parse_duration(duration[i])
        print(res)
        return res

    def play(self, note, pitch, duration, tempo):
        # define GPIO in BOARD mode, L1 to R5, the last one is useless
        # L:Left, R:Right; 1 to 5: thumb to little finger
        FINGER = [29,31,33,35,37,12,16,18,22,32,40] 

        # define SERVO parameter
        # duty=2.5--v +max
        # duty=7.5--v=0
        # duty=12.5-v -max
        freq = 50
        set =   [7.5,8   ,8   ,7.5 ,6.5 ,7.5,7.5 ,8   ,7   ,6.25,7.5]
        press = [7.5,7.2 ,7   ,9   ,8.25,7.5,7   ,7   ,8   ,7.25,7.5]
        back =  [7.5,8.5 ,8   ,7.5 ,7   ,7.5,8   ,7.75,7.05,6.25,7.5]

        # GPIO Init
        PWM = []
        GPIO.setmode(GPIO.BOARD)
        for i in FINGER:
            GPIO.setup(i,GPIO.OUT,initial=GPIO.LOW)
            PWM.append(GPIO.PWM(i,freq))     
        # HAND Init    
        for i in range(1,10):
            if i==5:
                continue
            PWM[i].start(press[i])
            time.sleep(0.5*60/tempo/2)
            PWM[i].ChangeDutyCycle(back[i])
            time.sleep(0.5*60/tempo/2)
            for j in range(0,1):
                PWM[i].ChangeDutyCycle(press[i])
                time.sleep(0.5*60/tempo/2)
                PWM[i].ChangeDutyCycle(back[i])
                time.sleep(0.5*60/tempo/2)
            PWM[i].ChangeDutyCycle(0)          
        
        #  the lowest
        base = input('the lowest note')
        base = int(base)

                               
        for i in range(len(note)):        
            if 0<note[i]<8 and duration[i]>0:
                play_note = (2-pitch[i])*7+note[i]                
                # already make sure there is no faster than eighth note   
                if (duration[i]>=3):
                    duration[i] = 2    
                    
                play_duration = 1/(2**(duration[i]-1))
                # extended notes
                j = 1
                while(i+j<len(note) and note[i+j] == 10):
                    j = j + 1
                    play_duration = play_duration + 1
                # dotted notes
                if (i+1<len(note) and note[i+1] == 9):
                    play_duration = 1.5 * play_duration  
                self.play_a_note(PWM,play_note,play_duration,press,back,tempo,base)             
            elif note[i] == 0:
                play_note = note[i]
                play_duration = 1/2**(duration[i]-1)  
                self.play_a_note(PWM,play_note,play_duration,press,back,tempo,base)
                 
        GPIO.cleanup()
   
    def play_a_note(self,PWM,note,duration,press,back,tempo,base=5):
        if note!=0:
            print([note,duration])
            PWM[self.note2finger(note,base)].ChangeDutyCycle(press[self.note2finger(note,base)])
            time.sleep(duration*60/tempo/2)
            PWM[self.note2finger(note,base)].ChangeDutyCycle(back[self.note2finger(note,base)])
            time.sleep(duration*60/tempo/2)
            PWM[self.note2finger(note,base)].ChangeDutyCycle(0)
            #if note != next_note:
            #    PWM[self.note2finger(note)].stop()     
        elif note == 0:
            time.sleep(duration*60/tempo)

    def parse_note(self, note):
        if (note <= 7 and note >= 0):
            return " " + str(note)
        elif note == 8:
            return " |"
        elif note == 9:
            return "."
        elif note == 10:
            return "-"

    def parse_duration(self, duration):
        if duration <= 1:
            return ""
        else:
            return (duration - 1) * "_"

    def parse_pitch(self, pitch):
        return str(5 - pitch)
    
    def note2finger(self, note, base):
        #base = 5            # low so
        if note == base:       
            return 1        # left index finger
        elif note == base+1:     
            return 2        # left middle finger
        elif note == base+2:    
            return 3        # left ring finger
        elif note == base+3:    
            return 4        # left little finger
        elif note == base+4:    
            return 6        # right index finger
        elif note == base+5:    
            return 7        # right middle finger
        elif note == base+6:    
            return 8        # right ring finger
        elif note == base+7:    
            return 9        # right little finger
        else:
            return 10       

