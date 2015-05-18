#!/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *
 
class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
 
        nameLabel = QLabel("URI")
        self.nameLine = QLineEdit()
        self.backButton = QPushButton("<-")
        self.webview = QWebView()
 
        HLayout1 = QHBoxLayout()
        HLayout1.addWidget(self.backButton)
        HLayout1.addWidget(nameLabel)
        HLayout1.addWidget(self.nameLine)
 
        self.nameLine.returnPressed.connect(self.requestUri)
        self.backButton.clicked.connect(self.goBack)
        self.webview.loadProgress.connect(self.loading)
        self.webview.loadFinished.connect(self.changePage)
 
        mainLayout = QGridLayout()
        mainLayout.addLayout(HLayout1, 0, 1)
        mainLayout.addWidget(self.webview, 1, 1)
 
        self.setLayout(mainLayout)
        self.setWindowTitle("sbrowser")
 
    def requestUri(self):
        url = QUrl(self.nameLine.text())
        if url.isValid():
            self.webview.load(url)
        else:
            self.setWindowTitle("URI not valid - sbrowser")

    def loading(self):
        self.setWindowTitle("Loading" + " - sbrowser")

    def changePage(self):
        self.setWindowTitle(self.webview.url().url() + " - sbrowser")
        self.nameLine.setText(self.webview.url().url())

    def goBack(self):
        self.webview.back()

if __name__ == '__main__':
    import sys
 
    app = QApplication(sys.argv)
 
    screen = Form()
    screen.show()
 
    sys.exit(app.exec_())
