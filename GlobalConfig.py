
#TODO:
#定义错误码 美化子界面
class Resourse:
    pass 

class GlobalConfig:
    dt = 50
    unit_height = 240
    
    hardware_tip_content = '''<html><head/><body><p><span style=" color:#ffffff; font-size:20px; font-family:等线 ">机械臂准备中，请稍后...</span></p></body></html>'''

    white_piano_width = 33
    white_piano_height = 100
    black_piano_width = 20 
    black_piano_height = 66

    @staticmethod
    def drop_speed_pixels_per_frame():
        return (GlobalConfig.unit_height * GlobalConfig.dt / MusicConfig.get_unit_interval_second() / 1000)
    @staticmethod
    def drop_speed_pixels_per_ms():
        return GlobalConfig.unit_height / MusicConfig.get_unit_interval_second() / 1000

    @staticmethod
    def interval():
        return 0.6 * GlobalConfig.unit_height

class MusicConfig:
    tempo = 80
    prefix = "./chords"

    @staticmethod
    def get_unit_interval_second():
        return 30 / MusicConfig.tempo
