# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 871, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1197, 28))
        self.menubar.setObjectName("menubar")
        self.menuMy_Desktop = QtWidgets.QMenu(self.menubar)
        self.menuMy_Desktop.setObjectName("menuMy_Desktop")
        self.menuFile_Manager = QtWidgets.QMenu(self.menubar)
        self.menuFile_Manager.setObjectName("menuFile_Manager")
        self.menuTask_Manager = QtWidgets.QMenu(self.menubar)
        self.menuTask_Manager.setObjectName("menuTask_Manager")
        MainWindow.setMenuBar(self.menubar)
        self.actionNotepad = QtWidgets.QAction(MainWindow)
        self.actionNotepad.setObjectName("actionNotepad")
        self.menuMy_Desktop.addAction(self.actionNotepad)
        self.menubar.addAction(self.menuMy_Desktop.menuAction())
        self.menubar.addAction(self.menuFile_Manager.menuAction())
        self.menubar.addAction(self.menuTask_Manager.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMy_Desktop.setTitle(_translate("MainWindow", "My Desktop"))
        self.menuFile_Manager.setTitle(_translate("MainWindow", "File Manager"))
        self.menuTask_Manager.setTitle(_translate("MainWindow", "Task Manager"))
        self.actionNotepad.setText(_translate("MainWindow", "Notepad"))

