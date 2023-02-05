# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 554)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icon_calc.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.functionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.functionEdit.setGeometry(QtCore.QRect(10, 10, 181, 21))
        self.functionEdit.setText("")
        self.functionEdit.setDragEnabled(False)
        self.functionEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.functionEdit.setClearButtonEnabled(False)
        self.functionEdit.setObjectName("functionEdit")
        self.functionList = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.functionList.setGeometry(QtCore.QRect(10, 60, 211, 411))
        self.functionList.setReadOnly(True)
        self.functionList.setObjectName("functionList")
        self.clearing = QtWidgets.QPushButton(self.centralwidget)
        self.clearing.setGeometry(QtCore.QRect(10, 480, 211, 31))
        self.clearing.setObjectName("clearing")
        self.plotForm = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plotForm.setGeometry(QtCore.QRect(229, 9, 502, 502))
        self.plotForm.setObjectName("plotForm")
        self.move_left = QtWidgets.QPushButton(self.centralwidget)
        self.move_left.setGeometry(QtCore.QRect(740, 40, 31, 31))
        self.move_left.setObjectName("move_left")
        self.movementGroup = QtWidgets.QButtonGroup(MainWindow)
        self.movementGroup.setObjectName("movementGroup")
        self.movementGroup.addButton(self.move_left)
        self.move_right = QtWidgets.QPushButton(self.centralwidget)
        self.move_right.setGeometry(QtCore.QRect(800, 40, 31, 31))
        self.move_right.setObjectName("move_right")
        self.movementGroup.addButton(self.move_right)
        self.move_up = QtWidgets.QPushButton(self.centralwidget)
        self.move_up.setGeometry(QtCore.QRect(770, 10, 31, 31))
        self.move_up.setObjectName("move_up")
        self.movementGroup.addButton(self.move_up)
        self.move_down = QtWidgets.QPushButton(self.centralwidget)
        self.move_down.setGeometry(QtCore.QRect(770, 70, 31, 31))
        self.move_down.setObjectName("move_down")
        self.movementGroup.addButton(self.move_down)
        self.magnify = QtWidgets.QPushButton(self.centralwidget)
        self.magnify.setGeometry(QtCore.QRect(750, 120, 71, 31))
        self.magnify.setObjectName("magnify")
        self.magnifierGroup = QtWidgets.QButtonGroup(MainWindow)
        self.magnifierGroup.setObjectName("magnifierGroup")
        self.magnifierGroup.addButton(self.magnify)
        self.shrink = QtWidgets.QPushButton(self.centralwidget)
        self.shrink.setGeometry(QtCore.QRect(750, 160, 71, 31))
        self.shrink.setObjectName("shrink")
        self.magnifierGroup.addButton(self.shrink)
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(200, 10, 21, 23))
        self.help.setObjectName("help")
        self.plotImage = QtWidgets.QLabel(self.centralwidget)
        self.plotImage.setGeometry(QtCore.QRect(230, 10, 501, 501))
        self.plotImage.setText("")
        self.plotImage.setObjectName("plotImage")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(10, 30, 201, 31))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionc = QtWidgets.QAction(MainWindow)
        self.actionc.setObjectName("actionc")
        self.saveAsPng = QtWidgets.QAction(MainWindow)
        self.saveAsPng.setObjectName("saveAsPng")
        self.saveInTable = QtWidgets.QAction(MainWindow)
        self.saveInTable.setObjectName("saveInTable")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.openFromTable = QtWidgets.QAction(MainWindow)
        self.openFromTable.setObjectName("openFromTable")
        self.openAbout = QtWidgets.QAction(MainWindow)
        self.openAbout.setObjectName("openAbout")
        self.helpAct = QtWidgets.QAction(MainWindow)
        self.helpAct.setObjectName("helpAct")
        self.menu.addAction(self.saveInTable)
        self.menu.addAction(self.openFromTable)
        self.menuFile.addAction(self.saveAsPng)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menu.menuAction())
        self.menuHelp.addAction(self.helpAct)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.openAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Графический калькулятор"))
        self.functionEdit.setPlaceholderText(_translate("MainWindow", "Введите функцию"))
        self.clearing.setText(_translate("MainWindow", "Очистить результаты расчетов"))
        self.move_left.setText(_translate("MainWindow", "←"))
        self.move_right.setText(_translate("MainWindow", "→"))
        self.move_up.setText(_translate("MainWindow", "↑"))
        self.move_down.setText(_translate("MainWindow", "↓"))
        self.magnify.setText(_translate("MainWindow", "Приблизить"))
        self.shrink.setText(_translate("MainWindow", "Отдалить"))
        self.help.setText(_translate("MainWindow", "?"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.menu.setTitle(_translate("MainWindow", "Журнал"))
        self.menuHelp.setTitle(_translate("MainWindow", "Справка"))
        self.actionc.setText(_translate("MainWindow", "c"))
        self.saveAsPng.setText(_translate("MainWindow", "Сохранить окно графиков как изображение"))
        self.saveInTable.setText(_translate("MainWindow", "Сохранить функции в журнале"))
        self.action.setText(_translate("MainWindow", "Сохранить как..."))
        self.openFromTable.setText(_translate("MainWindow", "Открыть функции из журнала"))
        self.openAbout.setText(_translate("MainWindow", "О программе"))
        self.helpAct.setText(_translate("MainWindow", "Помощь"))
