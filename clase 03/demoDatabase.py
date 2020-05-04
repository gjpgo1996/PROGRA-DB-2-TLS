# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 193)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditDBName = QtWidgets.QLineEdit(Dialog)
        self.lineEditDBName.setObjectName("lineEditDBName")
        self.horizontalLayout.addWidget(self.lineEditDBName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonCreateDB = QtWidgets.QPushButton(Dialog)
        self.pushButtonCreateDB.setObjectName("pushButtonCreateDB")
        self.verticalLayout.addWidget(self.pushButtonCreateDB)
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.verticalLayout.addWidget(self.labelResponse)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter database name"))
        self.pushButtonCreateDB.setText(_translate("Dialog", "Create Database"))

