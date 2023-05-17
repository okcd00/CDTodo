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
import sys
sys.path.append('./')

# basic packages
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# custom packages
from panel_with_browser import PanelBrowser
from panel_with_conferences import ConferenceBrowser
from file_io import * 


class threePanel(QWidget):
    def __init__(self):
        super(threePanel, self).__init__()
        self.setStyleSheet('''QWidget{background-color:#ee0000;}''')

        threePanel_layout = QHBoxLayout()
        qlabel = QLabel("这是界面3")
        threePanel_layout.addWidget(qlabel)

        self.setLayout(threePanel_layout)


class MemoryManager(QWidget):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.resize(
            self.desktop.width() // 4, 
            self.desktop.height() // 4)
        self.init_ui()

    def init_ui(self):
        # MainUI Panel
        self.mainPanel_layout = QHBoxLayout()

        # switch buttions
        self.button_layout = QVBoxLayout()
        select_Panel1_button = QPushButton("panel1")
        select_Panel2_button = QPushButton("panel2")
        select_Panel3_button = QPushButton("panel3")
        self.button_layout.addWidget(select_Panel1_button)
        self.button_layout.addWidget(select_Panel2_button)
        self.button_layout.addWidget(select_Panel3_button)

        # pages
        self.panel_browser = PanelBrowser()
        self.conference_browser = ConferenceBrowser()
        self.panel3 = threePanel()

        # stack layout
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(self.panel_browser)
        self.stack_layout.addWidget(self.conference_browser)
        self.stack_layout.addWidget(self.panel3)

        # main = button + stack
        self.mainPanel_layout.addLayout(self.button_layout)
        self.mainPanel_layout.addLayout(self.stack_layout)

        # connect switches with panels
        select_Panel1_button.clicked.connect(lambda: self.show_panel(select_Panel1_button))
        select_Panel2_button.clicked.connect(lambda: self.show_panel(select_Panel2_button))
        select_Panel3_button.clicked.connect(lambda: self.show_panel(select_Panel3_button))

        self.setLayout(self.mainPanel_layout)

        _flags = Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint 
        _flags |= Qt.SubWindow
        # _flags |= Qt.WindowTransparentForInput  # 鼠标穿透
        self.setWindowFlags(_flags)
        self.setAutoFillBackground(False)

    def show_panel(self, button):
        stack_pages = {
            "panel1": 0,
            "panel2": 1,
            "panel3": 2
        }
        index = stack_pages[button.text()]
        print(f"Switch to {index}")
        self.stack_layout.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mm = MemoryManager()
    mm.show()
    sys.exit(app.exec_())
    # mm.dump_memory()
