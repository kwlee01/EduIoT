#!/usr/bin/python3

import sys
#from PySide2 import QtCore, QtGui
from PySide2 import QtCore, QtWidgets


class LayoutWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Layout Window")
        hbox = QtWidgets.QHBoxLayout(self)
        vbox = QtWidgets.QVBoxLayout()
        label1 = QtWidgets.QLabel("Top")
        label2 = QtWidgets.QLabel("Bottom")
        label3 = QtWidgets.QLabel("Right")
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        hbox.addLayout(vbox)
        hbox.addWidget(label3)
        self.resize(150, 100)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    #button = QtGui.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    lw = LayoutWindow()
    lw.show()
    sys.exit(app.exec_())
