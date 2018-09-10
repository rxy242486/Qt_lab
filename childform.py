# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'childform.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_childform(object):
    def setupUi(self, childform):
        childform.setObjectName("childform")
        childform.resize(1200, 675)
        self.textEdit = QtWidgets.QTextEdit(childform)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 1181, 641))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(childform)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 89, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(childform)
        self.pushButton.clicked.connect(childform.close)
        QtCore.QMetaObject.connectSlotsByName(childform)

    def retranslateUi(self, childform):
        _translate = QtCore.QCoreApplication.translate
        childform.setWindowTitle(_translate("childform", "Form"))
        self.pushButton.setText(_translate("childform", "close"))

