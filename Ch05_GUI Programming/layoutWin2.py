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
        
        self.checkbox = QtWidgets.QCheckBox("CheckButton", self)
        self.checkbox.setObjectName("check")
        vbox.addWidget(self.checkbox)

        buttongroup = QtWidgets.QButtonGroup()
        self.radiobutton1 = QtWidgets.QRadioButton("RadioButton1", self)
        self.radiobutton1.setObjectName("radio1")
        buttongroup.addButton(self.radiobutton1)
        vbox.addWidget(self.radiobutton1)
        self.radiobutton2 = QtWidgets.QRadioButton("RadioButton2", self)
        self.radiobutton2.setObjectName("radio2")
        buttongroup.addButton(self.radiobutton2)
        vbox.addWidget(self.radiobutton2)
        self.radiobutton3 = QtWidgets.QRadioButton("RadioButton3", self)
        self.radiobutton3.setObjectName("radio3")
        buttongroup.addButton(self.radiobutton3)
        vbox.addWidget(self.radiobutton3)

        self.button = QtWidgets.QPushButton("OK", self)
        self.button.setObjectName("button")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.clicked)


        hbox.addLayout(vbox)

        self.combo = QtWidgets.QComboBox(self)
        self.combo.setObjectName("combo")
        self.combo.addItem("Apple")
        self.combo.addItem("Banana")
        self.combo.addItem("Grapes")
        self.combo.addItem("Mango")
        hbox.addWidget(self.combo)
        self.combo.activated[str].connect(self.activated)

        #label1 = QtWidgets.QLabel("Top")
        #label2 = QtWidgets.QLabel("Bottom")
        #label3 = QtWidgets.QLabel("Right")
        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #hbox.addLayout(vbox)
        #hbox.addWidget(label3)
        self.resize(150, 100)

    def printState(self, button):
        if button.isChecked():
            print(button.objectName(), "is checked")
        else :
            print(button.objectName(), "is not checked")

    def clicked(self):
        self.printState(self.checkbox)
        self.printState(self.radiobutton1)
        self.printState(self.radiobutton2)

    def activated(self, text):
        print(self.combo.objectName(), "is", text)


if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    #button = QtGui.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    lw = LayoutWindow()
    lw.show()
    sys.exit(app.exec_())
