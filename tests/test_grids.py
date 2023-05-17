
import sys

from PyQt5.QtWidgets import QApplication, QGridLayout, QMainWindow, QTextEdit, QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

url = "https://www.okcd00.tech"

app = QApplication(sys.argv)

w = QMainWindow()

browser = QWebEngineView()
browser.load(QUrl(url))

central_widget = QWidget()
w.setCentralWidget(central_widget)

lay = QGridLayout(central_widget)
lay.addWidget(browser, 0, 0, 2, 1)
lay.addWidget(QTextEdit(), 0, 1)
lay.addWidget(QTextEdit(), 1, 1)

lay.setColumnStretch(0, 1)
lay.setColumnStretch(1, 1)

lay.setRowStretch(0, 1)
lay.setRowStretch(1, 1)

w.show()

sys.exit(app.exec_())