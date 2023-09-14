import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QThread

import ShowUntil as showUntil
import UntilConfig as untilConfig
import LineController as lineFuncation
import PointController as PointFuncation

class DealShow(object):
    def __init__(self, excl_path, mdb_path):
        self.excl_path = excl_path
        untilConfig.excl_path = excl_path
        self.mdb_path = mdb_path
        untilConfig.mdb_path = mdb_path

        self.excl_cloum_path = ""
        self.table_list_data = []  # Initialize the list to store table names
        self.table_select = []  # Initialize the list to store selected tables

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

        # Connect signals and slots
        self.excl_cloum_button.clicked.connect(self.selectExclFile)
        self.all_quary.stateChanged.connect(self.selectAllTables)
        self.start_button.clicked.connect(self.dealData)
        self.table_list.itemChanged.connect(self.tableItemChanged)

    # 添加一个新的槽函数来处理多选框的状态变化
    def tableItemChanged(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            self.table_select.append(item.text())  # 添加到self.table_select
            print(self.table_select)
        else:
            if item.text() in self.table_select:
                self.table_select.remove(item.text())  # 从self.table_select中移除
                print(self.table_select)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "字段配置"))
        self.excl_cloum_button.setText(_translate("Form", "选择Excl文件"))
        self.groupBox_2.setTitle(_translate("Form", "选择表格"))
        self.start_button.setText(_translate("Form", "开始"))
        self.all_quary.setText(_translate("Form", "全选"))

        # Set initial state
        self.excl_cloum_text.setEnabled(False)
        self.all_quary.setEnabled(True)
        self.start_button.setEnabled(False)
        self.loadExclSheet()

        # Check all items in table_list and add them to table_select
        for i in range(self.table_list.count()):
            item = self.table_list.item(i)
            if item is not None:
                item.setCheckState(QtCore.Qt.Unchecked)

    def selectExclFile(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly  # Allow only reading the file
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "选择Excl文件", "",
                                                            "Excel Files (*.xls *.xlsx);;All Files (*)",
                                                            options=options)

        if fileName:
            self.excl_cloum_path = fileName
            untilConfig.excl_cloum_path = fileName
            self.loadExclText()
            self.start_button.setEnabled(True)

    def loadExclText(self):
        data_list = showUntil.getExclSheet(self.excl_cloum_path)
        str_data = "\n".join(data_list)
        self.excl_cloum_text.setPlainText("载入字段配置:\n" + str_data)

    def loadExclSheet(self):
        self.table_list.clear()  # Clear existing items
        self.table_list_data = showUntil.getExclSheet(self.excl_path)
        pattern = r'.*_(LINE|POINT)'
        filtered_data = [item for item in self.table_list_data if re.match(pattern, item)]
        self.table_list_data = filtered_data.copy()
        self.table_list.addItems(self.table_list_data)

    def selectAllTables(self):
        checked = self.all_quary.isChecked()
        if self.excl_cloum_path != "":
            self.start_button.setEnabled(True)

        if self.table_list.count() > 0:
            self.table_select = []  # 清空table_select列表
            for i in range(self.table_list.count()):
                item = self.table_list.item(i)
                if item is not None:
                    item.setCheckState(QtCore.Qt.Checked if checked else QtCore.Qt.Unchecked)
                    # 不再在这里手动添加/移除，而是在tableItemChanged槽函数中处理
    def dealData(self):
        self.theard=DataProcessingThread(self.progressBar,self.table_select,self.information_text,self.excl_cloum_path,self.start_button)
        self.theard.start()

class DataProcessingThread(QtCore.QThread):
    def __init__(self, progressBar, table_select, information_text, excl_cloum_path, start_button, parent=None):
        super(DataProcessingThread, self).__init__(parent)
        self.progressBar = progressBar
        self.table_select = table_select
        self.information_text = information_text
        self.excl_cloum_path = excl_cloum_path
        self.start_button = start_button

    def run(self):
        self.start_button.setEnabled(False)
        if len(self.table_select) != 0:
            self.progressBar.setMaximum(len(self.table_select))
            self.progressBar.setValue(0)
            num = 0
            for item in self.table_select:
                if re.search(r'_LINE$', item):
                    new_list, table_cloum = lineFuncation.initData(item, self.excl_cloum_path)
                    for i in new_list:
                        msg = lineFuncation.getMsg(item, table_cloum, i)
                        self.information_text.append("\n" + msg)
                        num += 1
                        self.progressBar.setValue(num)
                    print("Processing _LINE:", item)
                elif re.search(r'_POINT$', item):
                    new_list, table_cloum = PointFuncation.initData(item, self.excl_cloum_path)
                    for i in new_list:
                        msg = PointFuncation.getMsg(item, table_cloum, i)
                        self.information_text.append("\n" + msg)
                    num += 1
                    self.progressBar.setValue(num)
                    print("Processing _POINT:", item)


            self.information_text.append("\n" + "本次处理完成")
            self.start_button.setEnabled(True)

        else:
            self.information_text.append("没有选择数据")
            self.start_button.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = DealShow("path_to_excl", "path_to_mdb")  # Replace with your file paths
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
