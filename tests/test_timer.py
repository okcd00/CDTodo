
#!usr/bin/python
# -*- coding: utf-8 -*-
import time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLCDNumber, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QFont
import sys
 
 
class WinForm(QWidget):
 
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
 
        self.setWindowTitle("CDTimer demo")
        self.label = QLabel('排练计时')
        self.font = QFont()
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.label.setFont(self.font)
        self.startBtn = QPushButton('开始')
        self.pauseBtn = QPushButton('暂停')
        self.endBtn = QPushButton('结束')
 
        layout = QGridLayout(self)
        self.lcd_timer = QLCDNumber(self)
 
        # 初始化一个定时器
        self.timer = QTimer(self)
        self.start_time = 0
        self.is_pause = False
        # 将定时器超时信号与槽函数showTime()连接
        self.timer.timeout.connect(self.showTime)
 
        layout.addWidget(self.label, 0, 0, 2, 1)        
        layout.addWidget(self.lcd_timer, 0, 1, 2, 2)        
        layout.addWidget(self.startBtn, 2, 0)
        layout.addWidget(self.pauseBtn, 2, 1)
        layout.addWidget(self.endBtn, 2, 2)
        layout.setRowStretch(1, 1)
 
        # 连接按键操作和槽函数
        self.startBtn.clicked.connect(self.startTimer)
        self.pauseBtn.clicked.connect(self.pauseTimer)
        self.endBtn.clicked.connect(self.endTimer)
 
        self.setLayout(layout)
 
    def showTime(self):
        # 获取系统现在的时间
        # time = QDateTime.currentDateTime()
        # t = int(time.time() - self.start_time)
        # seconds = t % 60
        # minutes = (t // 60) % 60

        tstr = time.strftime("%X", time.gmtime(time.time() - self.start_time))
        self.lcd_timer.display(tstr)
 
    def startTimer(self):
        # 设置计时间隔并启动，每隔1000毫秒（1秒）发送一次超时信号，循环进行
        if not self.is_pause:
            self.start_time = time.time()
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.pauseBtn.setEnabled(True)
        self.endBtn.setEnabled(True)
    
    def pauseTimer(self):
        self.timer.stop()
        self.is_pause = True
        self.startBtn.setEnabled(True)
        self.pauseBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.is_pause = False
        self.startBtn.setEnabled(True)
        self.pauseBtn.setEnabled(False)
        self.endBtn.setEnabled(False)
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())