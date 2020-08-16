import sys
import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication,pyqtSignal,QObject
from PyQt5.uic import loadUi
from UI_SerialPanel import Ui_window

# 串口类
class SerialHelper(QWidget,Ui_window): # 传入UI文件Ui_window
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent) # 用super非显式的调用父类构造函数

        self.setupUi(self) # 设置UI
        self.setWindowTitle("串口助手---Pilot.Phil") # 设置窗口标题



if __name__=="__main__":
    app=QApplication(sys.argv)
    w=SerialHelper() # 实例化一个窗口对象SerialHelper
    w.show()
    sys.exit(app.exec_()) # 进入消息循环