from PyQt5 import QtCore,QtGui,QtWidgets
import sys 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
from childform import Ui_childform
from process_manager import Table
import threading
class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.child = childform()
        self.child1 = Table()
        self.actionNotepad.triggered.connect(self.openNotepad)
        self.actionTask_Manager.triggered.connect(self.opentaskmanager)
        self.actionClose_Window.triggered.connect(self.close)
        self.statusBar = QStatusBar()
        self.setStyleSheet("#MainWindow{border-image:url(bg1.jpg);}")
        self.setStatusBar(self.statusBar)
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.statusBar.showMessage(80*" "+text)
    def openNotepad(self):
        self.gridLayout.addWidget(self.child)
        self.child.show()

    def opentaskmanager(self):
        self.gridLayout.addWidget(self.child1)
        self.child1.show()
class childform(QtWidgets.QWidget,Ui_childform):
    def __init__(self):
        super(childform,self).__init__()
        self.setupUi(self)

class filemanager(QWidget):
    def __init__(self):
        super(filemanager,self).__init__()
    def show(self): 
        file_model = QFileSystemModel()
        file_model.setRootPath(QDir.currentPath())
        treeview = QTreeView()
        treeview.setModel(file_model)
        treeview.setRootIndex(file_model.index(QDir.currentPath()))
        treeview.resize(600,800)
        treeview.show()
class worker(QThread):
    def __init__(self,parent=None):
        super(worker,self).__init__()
        
app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
