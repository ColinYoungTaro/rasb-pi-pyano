from service import PredictorServiceInstance
from main_widget import UIWidget
from PyQt5.QtWidgets import QApplication
from control import HardWareController
import sys 

if __name__ == '__main__':
    HardWareController.init()
    PredictorServiceInstance() #init
    app = QApplication(sys.argv)
    ui = UIWidget()
    ui.show()
    # CameraDialog()
    sys.exit(app.exec_())
