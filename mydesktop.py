from PyQt5 import QtCore,QtGui,QtWidgets
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
from childform import Ui_childform
import threading
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.child = childform()
        self.actionNotepad.triggered.connect(self.openNotepad)

    def openNotepad(self):
        self.gridLayout.addWidget(self.child)
        self.child.show()
class childform(QtWidgets.QWidget,Ui_childform):
    def __init__(self):
        super(childform,self).__init__()
        self.setupUi(self)
app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
