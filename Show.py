# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Show.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 273)
        self.excl_button = QtWidgets.QPushButton(Form)
        self.excl_button.setGeometry(QtCore.QRect(380, 50, 91, 41))
        self.excl_button.setObjectName("excl_button")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 31))
        self.label.setObjectName("label")
        self.excl_lineEdit = QtWidgets.QLineEdit(Form)
        self.excl_lineEdit.setGeometry(QtCore.QRect(20, 50, 341, 41))
        self.excl_lineEdit.setObjectName("excl_lineEdit")
        self.mdb_lineEdit = QtWidgets.QLineEdit(Form)
        self.mdb_lineEdit.setGeometry(QtCore.QRect(20, 150, 341, 41))
        self.mdb_lineEdit.setObjectName("mdb_lineEdit")
        self.mdb_button = QtWidgets.QPushButton(Form)
        self.mdb_button.setGeometry(QtCore.QRect(380, 150, 91, 41))
        self.mdb_button.setObjectName("mdb_button")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.label_2.setObjectName("label_2")
        self.next_button = QtWidgets.QPushButton(Form)
        self.next_button.setGeometry(QtCore.QRect(20, 220, 451, 41))
        self.next_button.setObjectName("next_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.excl_button.setText(_translate("Form", "浏览"))
        self.label.setText(_translate("Form", "选择数据excl文件"))
        self.mdb_button.setText(_translate("Form", "浏览"))
        self.label_2.setText(_translate("Form", "选择数据库.mdb文件"))
        self.next_button.setText(_translate("Form", "下一步"))


# -*- coding: utf-8 -*-
import sys

# Form implementation generated from reading ui file 'Show.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QWidget, QStackedWidget
from PyQt5 import QtWidgets
# from QCandyUi.CandyWindow import createWindow
from DealShow import DealShow as wuhu

class MyDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 创建多个页面
        self.page1 = QWidget()
        self.page2 = QWidget()

        # 创建一个堆叠窗口
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.page1)
        self.stackedWidget.addWidget(self.page2)

        # 连接按钮点击事件到相应的槽函数
        self.ui.excl_button.clicked.connect(self.browseExclFile)
        self.ui.mdb_button.clicked.connect(self.browseMdbFile)
        self.ui.next_button.clicked.connect(self.nextPage)

    def browseExclFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择数据excl文件", "", "Excel Files (*.xlsx *.xls);;All Files (*)", options=options)
        if file_name:
            self.ui.excl_lineEdit.setText(file_name)
            self.stackedWidget.setCurrentIndex(1)  # 切换到下一个页面

    def browseMdbFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择数据库.mdb文件", "", "MDB Files (*.mdb);;All Files (*)", options=options)
        if file_name:
            self.ui.mdb_lineEdit.setText(file_name)
            self.stackedWidget.setCurrentIndex(1)  # 切换到下一个页面

    def nextPage(self):
        # Check if excl_lineEdit and mdb_lineEdit both have content
        excl_path = self.ui.excl_lineEdit.text()
        mdb_path = self.ui.mdb_lineEdit.text()

        if excl_path and mdb_path:
            # Create an instance of ShowDealWindow and set it as the current page in the stackedWidget
            # self.show_deal_window = createWindow(ShowDealWindow(excl_path, mdb_path),title="上传")
            self.show_deal_window = ShowDealWindow(excl_path, mdb_path)
            self.show_deal_window.show()
        else:
            QMessageBox.warning(self, "警告", "请先选择数据excl文件和数据库.mdb文件")


class ShowDealWindow(QMainWindow):
    def __init__(self,excl_path,mdb_path):
        super().__init__()
        self.ui = wuhu(excl_path,mdb_path)
        self.ui.setupUi(self)


# from QCandyUi.CandyWindow import createWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # dialog = createWindow(MyDialog(), title="上传",ico_path="AI.png")
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())

