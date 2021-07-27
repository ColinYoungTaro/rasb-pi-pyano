from singleton import Singleton
from note import Note
import numpy
import RPi.GPIO as GPIO
import time

# finger 的IO接口
FINGER = [29,31,33,35,37,12,16,18,22,32,40] 

s = [x for x in range(1,10)]
# PWM freq
freq = 50

vp = 8  # v positive
vn = 7  # v negative
press = [7.5,7.2 ,7   ,9   ,8.25,7.5,7   ,7   ,8   ,7.25,7.5]
back =  [7.5,8.5 ,8   ,7.5 ,7   ,7.5,8   ,7.75,7.05,6.25,7.5]



class HardWareController:
    # 初始化弹琴机械臂的IO口
    PWM = []
    base = 5
    def init():
        GPIO.setmode(GPIO.BOARD)
        for i in FINGER:
            GPIO.setup(i,GPIO.OUT,initial=GPIO.LOW)
            HardWareController.PWM.append(GPIO.PWM(i,freq))
            print("init ready")
        for index,pwm in enumerate(HardWareController.PWM):
            pwm.start(0)
    
    @staticmethod
    # 设置弹琴机械臂的基准
    def set_base(base):
        HardWareController.base = base

    def add_base():
        if HardWareController.base < 14:
            HardWareController.base += 1 

    def minus_base():
        if HardWareController.base > 0:
            HardWareController.base -= 1 

    def get_base():
        return HardWareController.base

    # 根据当前的base将需要弹奏的note转化为第几个按键在按
    def note2finger(note:int):
        if note >= HardWareController.base and note <= HardWareController.base + 3:
            return note - HardWareController.base + 1
        elif note <= HardWareController.base + 7:
            return note - HardWareController.base + 2
        else:
            return 10 
    
    def note_press(note:int):
        HardWareController.PWM[HardWareController.note2finger(note)].ChangeDutyCycle(press[HardWareController.note2finger(note)])
        #time.sleep(0.1)
    
    def note_release(note:int):
        HardWareController.PWM[HardWareController.note2finger(note)].ChangeDutyCycle(back[HardWareController.note2finger(note)])
        #time.sleep(0.1)

    def note_idle(note:int):
        HardWareController.PWM[HardWareController.note2finger(note)].ChangeDutyCycle(0)

    def move_base(base:int):
        print("move start")
        time.sleep(5)
        print("move end")


    # 析构函数
    def dispose():
        for pwm in HardWareController.PWM:
            pwm.stop()
        GPIO.cleanup() 
        pass


