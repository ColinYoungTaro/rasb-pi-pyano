import numpy
import RPi.GPIO as GPIO
import time

# finger 的IO接口
FINGER = [29,31,33,35,37,12,16,18,22,32,40] 

s = [x for x in range(1,10)]
# PWM freq
freq = 50
# music tempo
tempo = 80
vp = 8  # v positive
vn = 7  # v negative
press = [7.5,7.2 ,7   ,9   ,8.25,7.5,7   ,7   ,8   ,7.25,7.5]
back =  [7.5,8.5 ,8   ,7.5 ,7   ,7.5,8   ,7.75,7.05,6.25,7.5]

class HardWareController:
    # 初始化弹琴机械臂的IO口
    def __init__(self):
        self.PWM = []
        self.base = 5
        GPIO.setmode(GPIO.BOARD)
        for i in FINGER:
            GPIO.setup(i,GPIO.OUT,initial=GPIO.LOW)
            self.PWM.append(GPIO.PWM(i,freq))

        self.init_pwm()
    
    def init_pwm(self):
        for index,pwm in enumerate(self.PWM):
            pwm.start(0)


    # 设置弹琴机械臂的基准
    def set_base(self,base):
        self.base = base

    def get_base(self):
        return self.base

    # 根据当前的base将需要弹奏的note转化为第几个按键在按
    def note2finger(self,note:int):
        if note >= self.base and note <= self.base + 3:
            return note - self.base + 1
        elif note <= self.base + 7:
            return note - self.base + 2
        else:
            return 10 

    def note_press(self,note):
        self.PWM[self.note2finger(note.abs_int_note)].ChangeDutyCycle(press[self.note2finger(note)])

    def note_release(self,note):
        self.PWM[self.note2finger(note.abs_int_note)].ChangeDutyCycle(back[self.note2finger(note)])

    # 析构函数
    def dispose(self):
        for pwm in self.PWM:
            pwm.stop()
        GPIO.cleanup() 
