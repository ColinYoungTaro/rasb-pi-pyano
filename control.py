from singleton import Singleton
from note import Note
import numpy
import RPi.GPIO as GPIO
import time

# finger 的IO接口
FINGER = [12,16,18,22,32,29,31,33,35,37,36]

s = [x for x in range(1,10)]
# PWM freq
freq = 50

press = [7.5,7.5 ,6.75,8.5 ,8.25,7.5,7   ,6.75,8.05,7.25,7.5]
back =  [7.5,8.5 ,8   ,7.25,7   ,7.5,8.25,7.75,7.05,6.25,7.5]

# driver IO
Driver_PUL = 38
Driver_DIR = 40
Driver_Freq = 1e4


class HardWareController:
    # 初始化弹琴机械臂&driver的IO口
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

        # driver
        HardWareController.last_base = 8 # middle do        
        # print("driver init begin")
        GPIO.setup(Driver_PUL,GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(Driver_DIR,GPIO.OUT,initial=GPIO.HIGH)
        HardWareController.PWM_PUL = GPIO.PWM(Driver_PUL,Driver_Freq)
        # HardWareController.PWM_PUL.start(0)
        # print("driver init end")

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

        # print(HardWareController.last_base, base)
        # HardWareController.move_hand(last_base=HardWareController.last_base, base=base)
        # HardWareController.last_base = base
        time.sleep(2)
        print("move end")

    def move_hand(last_base:int, base:int):
        if base>=last_base:
            GPIO.output(Driver_DIR,GPIO.HIGH)
        else:
            GPIO.output(Driver_DIR,GPIO.LOW)            
        HardWareController.PWM_PUL.start(50)
        time.sleep(abs(base-last_base)*1.58)
        # clean up
        HardWareController.PWM_PUL.ChangeDutyCycle(0)   
        GPIO.output(Driver_DIR,GPIO.LOW) 

    # 析构函数
    def dispose():
        for pwm in HardWareController.PWM:
            pwm.stop()
        HardWareController.move_hand(last_base=HardWareController.last_base, base=8)
        HardWareController.PWM_PUL.stop()
        GPIO.cleanup() 
        pass


