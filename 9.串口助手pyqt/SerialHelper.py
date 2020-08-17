import sys
import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication,pyqtSignal,QObject
from PyQt5.uic import loadUi
from UI_SerialPanel import Ui_window

# 串口类
class SerialHelper(QWidget): # 传入UI文件Ui_window

    ms=sig()

    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent) # 用super非显式的调用父类构造函数

        self.ui = Ui_window()
        self.ui.setupUi(self) # 设置UI
        self.setWindowTitle("串口助手---Pilot.Phil") # 设置窗口标题

    def do(self):
        print("mysignal did")




if __name__=="__main__":
    app=QApplication(sys.argv)
    w=SerialHelper() # 实例化一个窗口对象SerialHelper
    w.show()
    sys.exit(app.exec_()) # 进入消息循环