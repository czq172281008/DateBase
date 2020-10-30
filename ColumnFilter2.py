# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColumnFilter2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColumnFilter(object):

    def setupUi(self, ColumnFilter):
        ColumnFilter.setObjectName("ColumnFilter")
        ColumnFilter.resize(1022, 824)
        self.tableWidget = QtWidgets.QTableWidget(ColumnFilter)
        self.tableWidget.setGeometry(QtCore.QRect(80, 160, 821, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(ColumnFilter)
        self.label.setGeometry(QtCore.QRect(60, 80, 101, 31))
        self.label.setObjectName("label")
        self.toolButton_2 = QtWidgets.QPushButton(ColumnFilter)
        self.toolButton_2.setGeometry(QtCore.QRect(680, 70, 75, 23))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton = QtWidgets.QPushButton(ColumnFilter)
        self.toolButton.setGeometry(QtCore.QRect(790, 70, 75, 23))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(ColumnFilter)
        QtCore.QMetaObject.connectSlotsByName(ColumnFilter)

    def retranslateUi(self, ColumnFilter):
        _translate = QtCore.QCoreApplication.translate
        ColumnFilter.setWindowTitle(_translate("ColumnFilter", "Form"))
        self.label.setText(_translate("ColumnFilter", "Table: None"))
        self.toolButton_2.setText(_translate("ColumnFilter", "txt"))
        self.toolButton.setText(_translate("ColumnFilter", "Data"))
