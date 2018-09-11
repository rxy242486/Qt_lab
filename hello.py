from PyQt5 import QtWidgets,QtGui
import sys

from dialog import Ui_Dialog
class mydialog(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(mydialog,self).__init__()
        self.setupUi(self)

    def hello(self):
        self.textEdit.setText("Hello world")

    def nihao(self):
        self.textEdit.setText("nihao")

