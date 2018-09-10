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
        MainWindow.resize(1029, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1021, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 28))
        self.menubar.setObjectName("menubar")
        self.menuMy_Desktop = QtWidgets.QMenu(self.menubar)
        self.menuMy_Desktop.setObjectName("menuMy_Desktop")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNotepad = QtWidgets.QAction(MainWindow)
        self.actionNotepad.setObjectName("actionNotepad")
        self.actionFile_Manager = QtWidgets.QAction(MainWindow)
        self.actionFile_Manager.setObjectName("actionFile_Manager")
        self.actionTask_Manager = QtWidgets.QAction(MainWindow)
        self.actionTask_Manager.setObjectName("actionTask_Manager")
        self.menuMy_Desktop.addAction(self.actionNotepad)
        self.menuMy_Desktop.addAction(self.actionFile_Manager)
        self.menuMy_Desktop.addAction(self.actionTask_Manager)
        self.menubar.addAction(self.menuMy_Desktop.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMy_Desktop.setTitle(_translate("MainWindow", "My Desktop"))
        self.actionNotepad.setText(_translate("MainWindow", "Notepad"))
        self.actionFile_Manager.setText(_translate("MainWindow", "File Manager"))
        self.actionTask_Manager.setText(_translate("MainWindow", "Task Manager"))

