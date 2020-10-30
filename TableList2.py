# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableList2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableList2(object):
    def setupUi(self, TableList2):
        TableList2.setObjectName("TableList2")
        TableList2.resize(788, 893)
        self.listWidget = QtWidgets.QListWidget(TableList2)
        self.listWidget.setGeometry(QtCore.QRect(50, 160, 351, 421))
        self.listWidget.setObjectName("listWidget")
        self.textBrowser = QtWidgets.QTextBrowser(TableList2)
        self.textBrowser.setGeometry(QtCore.QRect(50, 30, 301, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.toolButton = QtWidgets.QToolButton(TableList2)
        self.toolButton.setGeometry(QtCore.QRect(420, 80, 71, 20))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(TableList2)
        self.toolButton_2.setGeometry(QtCore.QRect(420, 50, 71, 18))
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(TableList2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(14, 640, 731, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homePage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.homePage.setObjectName("homePage")
        self.horizontalLayout.addWidget(self.homePage)
        self.prePage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.prePage.setObjectName("prePage")
        self.horizontalLayout.addWidget(self.prePage)
        self.curPage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.curPage.setObjectName("curPage")
        self.horizontalLayout.addWidget(self.curPage)
        self.nextPage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.nextPage.setObjectName("nextPage")
        self.horizontalLayout.addWidget(self.nextPage)
        self.finalPage = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.finalPage.setObjectName("finalPage")
        self.horizontalLayout.addWidget(self.finalPage)
        self.totalPage = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.totalPage.setObjectName("totalPage")
        self.horizontalLayout.addWidget(self.totalPage)
        self.skipLable_0 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.skipLable_0.setObjectName("skipLable_0")
        self.horizontalLayout.addWidget(self.skipLable_0)
        self.skipPage = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.skipPage.setEnabled(True)
        self.skipPage.setMinimumSize(QtCore.QSize(0, 0))
        self.skipPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.skipPage.setObjectName("skipPage")
        self.horizontalLayout.addWidget(self.skipPage)
        self.skipLabel_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.skipLabel_1.setObjectName("skipLabel_1")
        self.horizontalLayout.addWidget(self.skipLabel_1)
        self.confirmSkip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.confirmSkip.setObjectName("confirmSkip")
        self.horizontalLayout.addWidget(self.confirmSkip)

        self.retranslateUi(TableList2)
        QtCore.QMetaObject.connectSlotsByName(TableList2)

    def retranslateUi(self, TableList2):
        _translate = QtCore.QCoreApplication.translate
        TableList2.setWindowTitle(_translate("TableList2", "Form"))
        self.toolButton.setText(_translate("TableList2", "clear"))
        self.toolButton_2.setText(_translate("TableList2", "txt"))
        self.homePage.setText(_translate("TableList2", "首页"))
        self.prePage.setText(_translate("TableList2", "上一页"))
        self.curPage.setText(_translate("TableList2", "1"))
        self.nextPage.setText(_translate("TableList2", "下一页"))
        self.finalPage.setText(_translate("TableList2", "尾页"))
        self.totalPage.setText(_translate("TableList2", "共页"))
        self.skipLable_0.setText(_translate("TableList2", "跳到"))
        self.skipLabel_1.setText(_translate("TableList2", "页"))
        self.confirmSkip.setText(_translate("TableList2", "确定"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Columns = QtWidgets.QWidget()
    ui = Ui_TableList2()
    ui.setupUi(Columns)
    Columns.show()
    sys.exit(app.exec_())