# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : memory_manager.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-25
#   desc     : record and restore todo from local files
#              for registering and easy-modification
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


class MemoryManager(object):
    MEMORY_FORM = 'pkl file'
    MEMORY_FILE = 'compress json'
    MEMORY_PATH = 'memory/todo_memory'

    def __init__(self):
        # list indexing for all memories
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.browser = QWebEngineView()
        self.init_ui()

        # data
        self.data_list = None
        self.tag_mapping = defaultdict(list)  # tag: [index1, index2]
        self.time_mapping = defaultdict(list)  # time: [index1, index2]
        self.load_memory()

    def log(self, *args):
        print(*args)

    def refresh_page(self):
        url="https://www.okcd00.tech/about"
        self.browser.load(QUrl(url))

    def exit(self):
        self.window.close()
        sys.exit()

    def show_text(self):
        self.qte_read.setPlainText("呆咖喱")

    def remember_text_and_show(self):
        txt = self.qte_write.toPlainText()
        self.qte_read.setPlainText(txt)

    def init_ui(self, width=2, height=5):
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)

        # layout
        self.layout = QGridLayout(central_widget)
        self.layout.addWidget(self.browser, 0, 0, 4, 1)    
        self.btn_refresh = QPushButton("刷新")
        self.layout.addWidget(self.btn_refresh, 4, 0)
        
        self.qte_read = QTextEdit()
        self.layout.addWidget(self.qte_read, 0, 1)
        self.qte_read.setReadOnly(True)
        self.btn_show = QPushButton("展示")
        self.layout.addWidget(self.btn_show, 1, 1)
        self.qte_write = QTextEdit()
        self.qte_write.setFontFamily("黑体")
        self.qte_write.setFontPointSize(30)
        self.layout.addWidget(self.qte_write, 2, 1)
        self.btn_submit = QPushButton("提交")
        self.layout.addWidget(self.btn_submit, 3, 1)
        self.btn_exit = QPushButton("退出")
        self.layout.addWidget(self.btn_exit, 4, 1)
        
        # functions
        self.btn_refresh.clicked.connect(self.refresh_page)
        self.btn_show.clicked.connect(self.show_text)
        self.btn_submit.clicked.connect(self.remember_text_and_show)
        self.btn_exit.clicked.connect(self.exit)

        for col_idx in range(width):
            self.layout.setColumnStretch(col_idx, 1)
        
        for row_idx in range(height):
            self.layout.setRowStretch(row_idx, 1)

        _flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow
        # _flags |= Qt.WindowTransparentForInput
        self.window.setWindowFlags(_flags)
        self.window.setAutoFillBackground(False)

    def load_memory(self):
        # load with memory file selection
        if 'pkl' in self.MEMORY_FORM.split():
            self.data_list = load_pkl(self.MEMORY_PATH + '.pkl')
        elif 'kari' in self.MEMORY_FORM.split():
            dic = load_kari(self.MEMORY_PATH + '.kari')
            self.data_list = OrderedDict(dic)
        else:
            ls = load_vocab(self.MEMORY_PATH + '.txt')
            self.data_list = ls
        for index, item in enumerate(self.data_list):
            self.tag_mapping[item.get('tag', 'notag')].append(index)
            self.time_mapping[item.get('timestamp', -1)].append(index)
        self.log(f"Memory Loaded, {len(self.data_list)} todos are collected.")

    def dump_memory(self):
        # call it with the 'save' button (or maybe auto-save?)
        if 'pkl' in self.MEMORY_FORM.split():
            save_pkl(self.data_list, self.MEMORY_PATH + '.pkl')

    def show_manager_widget(self):
        url = "https://www.okcd00.tech"
        self.browser.load(QUrl(url))
        self.window.show()
        sys.exit(self.app.exec_())

    def insert_new_todo(self):
        pass

    def remove_todo(self):
        pass


if __name__ == "__main__":
    mm = MemoryManager()
    mm.show_manager_widget()
    mm.window.show()
    sys.exit(mm.app.exec_())
    # mm.dump_memory()
