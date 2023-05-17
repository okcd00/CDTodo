# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : panel_with_conference.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-05-17
#   desc     : 
#              
# ==========================================================================
# basic packages
from queue import PriorityQueue
from collections import OrderedDict, defaultdict
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

# custom packages
from todo_definition import Todo
from file_io import *
from memory_utils import *


class ConferenceBrowser(QWidget):

    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()

        # data
        self.data_list = []
        self.init_layout()

    def log(self, *args):
        print(*args)

    def init_layout(self):
        # layout
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.browser, 0, 0, 4, 2)    
        self.btn_refresh = QPushButton("进入网址")
        self.layout.addWidget(self.btn_refresh, 4, 1)
        self.qte_url = QTextEdit()
        self.qte_url.setFontFamily("Times New Roman")
        self.qte_url.setFontPointSize(14)
        self.qte_url.setMinimumHeight(15)
        self.qte_url.setMaximumHeight(30)
        self.layout.addWidget(self.qte_url, 4, 0)

        # functions
        self.btn_refresh.clicked.connect(self.refresh_page)

        self.layout.setColumnStretch(0, 1)
        self.layout.setRowStretch(0, 1)

        self.setLayout(self.layout)

    def refresh_page(self):
        url = "https://aideadlin.es/?sub=ML,NLP,DM"
        input_url = self.qte_url.toPlainText()
        if input_url.strip():
            url = input_url
        if not url.startswith('http'):
            url = 'https://' + url
        self.browser.load(QUrl(url))

    def exit(self):
        dump_memory(self)
        self.close()
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pb = ConferenceBrowser()
    url = "https://aideadlin.es/?sub=ML,NLP,DM"
    pb.browser.load(QUrl(url))
    pb.show()
    sys.exit(app.exec_())