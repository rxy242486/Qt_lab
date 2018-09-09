from PyQt5 import QtWidgets,QtGui
import sys

from dialog import Ui_Dialog
class mywindow(QtWidgets.QWidget,Ui_Dialog):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

    def hello(self):
        self.textEdit.setText("Hello world")

    def nihao(self):
        self.textEdit.setText("nihao")

app = QtWidgets.QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
