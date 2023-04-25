# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : CDTodo.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-25
#   desc     : Main entrance of the application
#
# ==========================================================================
import os, sys
from settings import PROJECT_PATH

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

from src.memory_manager import MemoryManager


class CDTodo(QWidget):
    # FILE_PREFIX = f"file:///"
    FILE_PREFIX = f"file:///{PROJECT_PATH}/"

    def __init__(self):
        super().__init__()
        self.memory_manager = MemoryManager()
        self.screen = QDesktopWidget().screenGeometry()
        self.init_ui()
        self.tray()

        self.timer = QTimer()
        print("Init Finished.")
    
    def init_ui(self, click_through=False):
        self.desktop_width = self.screen.width()
        self.desktop_height = self.screen.height()
        print(f"Current Desktop Size: {self.desktop_width}x{self.desktop_height}")
        _w, _h = 400, 300
        self.w = self.desktop_width // 2 - _w // 2
        self.h = self.desktop_height // 2 - _h // 2
        self.setGeometry(self.w, self.h, _w, _h)

        # Create a QWebEngineView and set it as the central widget
        self.browser = QWebEngineView(self)

        _flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow
        if click_through:  # 鼠标穿透
            _flags |= Qt.WindowTransparentForInput
        self.setWindowFlags(_flags)
        self.setAutoFillBackground(False)
        
        # 主画板窗体透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.show()

    def rpath(self, *args):
        uri = os.path.join(self.FILE_PREFIX, *args)
        print(uri)
        return uri

    def tray(self):
        tp = QSystemTrayIcon(self)
        icon_uri = self.rpath('/assets/cd_logo.png')
        tp.setIcon(QIcon(icon_uri))
        action_quit = QAction('Exit', self, triggered=self.quit)
        tpMenu = QMenu(self)
        tpMenu.addAction(action_quit)
        tp.setContextMenu(tpMenu)
        tp.show()

    def quit(self):
        self.close()
        sys.exit()

    def load_uri(self, uri=f'/assets/sample.html'):
        # load html page from files
        uri = self.rpath(uri)
        self.browser.load(QUrl.fromLocalFile(uri))

    def load_url(self, url='https://www.okcd00.tech'):
        # load html page from links
        # self.browser.load(QUrl('https://www.okcd00.tech'))
        self.browser.load(QUrl(url))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CDTodo()
    window.load_uri()
    window.show()
    sys.exit(app.exec_())