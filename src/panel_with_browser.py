# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : panel_with_browser.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-26
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


class PanelBrowser(QWidget):
    MEMORY_FORM = 'pkl file'
    MEMORY_FILE = 'compress json'
    MEMORY_PATH = 'memory/todo_memory'

    def __init__(self):
        super().__init__()
        # self.setStyleSheet('''QWidget{background-color:#66CCFF;}''')
        self.browser = QWebEngineView()

        # data
        self.data_list = []
        self.tag_mapping = defaultdict(list)  # tag: [index1, index2]
        self.time_mapping = defaultdict(list)  # time: [index1, index2]
        self.color_mapping = load_kari(
            'misc/tags_priority.kari', 
            show_time=True, single_item=True)
        
        load_memory(self)
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
        self.qte_url.setFontPointSize(15)
        self.qte_url.setMinimumHeight(15)
        self.qte_url.setMaximumHeight(30)
        # self.qte_url.setFixedHeight(self.btn_refresh.height())
        self.layout.addWidget(self.qte_url, 4, 0)
        
        self.qte_read = QTextEdit()
        self.layout.addWidget(self.qte_read, 0, 2)
        self.qte_read.setReadOnly(True)
        self.btn_show = QPushButton("展示")
        self.layout.addWidget(self.btn_show, 1, 2)
        self.qte_write = QTextEdit()
        self.qte_write.setFontFamily("微软雅黑")
        self.layout.addWidget(self.qte_write, 2, 2)
        self.btn_submit = QPushButton("提交")
        self.layout.addWidget(self.btn_submit, 3, 2)
        self.btn_exit = QPushButton("退出")
        self.layout.addWidget(self.btn_exit, 4, 2)

        # functions
        self.btn_refresh.clicked.connect(self.refresh_page)
        self.btn_show.clicked.connect(self.show_text)
        self.btn_submit.clicked.connect(self.submit)
        self.btn_exit.clicked.connect(self.exit)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(0, 1)

        self.setLayout(self.layout)

    def show_text(self):
        show_items = []
        for item in self.data_list:
            title = item.title or 'no-title'
            tag = item.tag or 'no-tag'
            color = self.color_mapping.get(tag, 'black')
            # show_items.append(title)
            show_items.append(f'<li><font color="{color}"> {title} </font><\li>\n')
        # show_text = "\n".join(show_items)
        # self.qte_read.setPlainText("show_text")
        show_text = "<p>TODOList: </p>\n"
        show_text += '<ul type="circle">\n' + "".join(show_items) + '</ul>'
        self.qte_read.setHtml(show_text)
        self.resize_qte_height(self.qte_read)

    def resize_qte_height(self, qte):
        content_size = qte.document().size()
        qte.setFixedHeight(content_size.height() + 20)

    def submit(self):
        txt = self.qte_write.toPlainText()
        self.qte_write.clear()
        self.insert_new_todo(txt)
        self.qte_read.setPlainText("Submitted: " + txt)
        self.resize_qte_height(self.qte_read)

    def refresh_page(self):
        url = "https://www.okcd00.tech/archives"
        input_url = self.qte_url.toPlainText()
        if input_url.strip():
            url = input_url
        if not url.startswith('http'):
            url = 'https://' + url
        self.browser.load(QUrl(url))
    
    def insert_new_todo(self, text):
        item = Todo(text)
        index = len(self.data_list)
        self.data_list.append(item)
        self.tag_mapping[item.tag].append(index)
        self.time_mapping[item.end_time].append(index)

    def remove_todo(self):
        pass

    def exit(self):
        dump_memory(self)
        self.close()
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pb = PanelBrowser()
    url = "https://www.okcd00.tech/archives/"
    pb.browser.load(QUrl(url))
    pb.show()
    sys.exit(app.exec_())