# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DealShow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(578, 477)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 211, 261))
        self.groupBox.setObjectName("groupBox")
        self.excl_cloum_text = QtWidgets.QTextEdit(self.groupBox)
        self.excl_cloum_text.setGeometry(QtCore.QRect(20, 70, 171, 171))
        self.excl_cloum_text.setObjectName("excl_cloum_text")
        self.excl_cloum_button = QtWidgets.QPushButton(self.groupBox)
        self.excl_cloum_button.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.excl_cloum_button.setObjectName("excl_cloum_button")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 290, 561, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 311, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.start_button = QtWidgets.QPushButton(self.groupBox_2)
        self.start_button.setGeometry(QtCore.QRect(140, 210, 121, 31))
        self.start_button.setObjectName("start_button")
        self.table_list = QtWidgets.QListWidget(self.groupBox_2)
        self.table_list.setGeometry(QtCore.QRect(50, 30, 211, 171))
        self.table_list.setObjectName("table_list")
        self.all_quary = QtWidgets.QCheckBox(self.groupBox_2)
        self.all_quary.setGeometry(QtCore.QRect(60, 200, 91, 51))
        self.all_quary.setObjectName("all_quary")
        self.information_text = QtWidgets.QTextEdit(Form)
        self.information_text.setGeometry(QtCore.QRect(20, 330, 531, 131))
        self.information_text.setObjectName("information_text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "字段配置"))
        self.excl_cloum_button.setText(_translate("Form", "载入配置Excl字段文件"))
        self.groupBox_2.setTitle(_translate("Form", "选择表格"))
        self.start_button.setText(_translate("Form", "开始"))
        self.all_quary.setText(_translate("Form", "全选"))

        # 设置初始状态
        self.excl_cloum_text.setEnabled(False)
        self.all_quary.setEnabled(False)
        self.start_button.setEnabled(False)

        # 这里是事件
