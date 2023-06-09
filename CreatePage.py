import os, datetime, re, shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QMessageBox

from CustomPyQt import CustomMainWindow, CustomTableWidget, CustomButton
from Functions import CreateFilePath
from Popups import show_info_popup
from CalculatePage import Ui_CalculateWindow

home_dir, file_path_to_HEC =CreateFilePath()

class Ui_CreatePage(object):
    def __init__(self, TextsForData):
        self.TextsForData = TextsForData
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 560)
        MainWindow.setMinimumSize(QtCore.QSize(1480, 560))
        MainWindow.setMaximumSize(QtCore.QSize(1480, 560))
        MainWindow.setStyleSheet("""
    QTableWidget QHeaderView::section {
        background-color: #F0F0F0;
        color: black;
        padding: 4px;
        font-weight: bold;
        border-right: 1px solid #D0D0D0;  /* Add a thin line between the column names */
        border-top: 1px solid #F0F0F0;
        border-bottom: 1px solid #F0F0F0;
    }

    QTableWidget QHeaderView::section:first {  /* Add this block to change the first column border */
        border-left: 1px solid #F0F0F0;
    }

    QTableWidget QTableCornerButton::section {  /* Add this block to change the corner button color */
        background-color: #F0F0F0;
        border: none;
        border-right: 1px solid #D0D0D0;  /* Add a thin line to the right */
        border-bottom: 1px solid #D0D0D0;  /* Add a thin line at the bottom */
    }
""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 40)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_7)
        self.frame_2.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_7)
        self.frame_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(570, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(570, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(7, 52, 96);")
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_Pname = QtWidgets.QLabel(self.frame_9)
        self.label_Pname.setMinimumSize(QtCore.QSize(170, 0))
        self.label_Pname.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Pname.setFont(font)
        self.label_Pname.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_Pname.setObjectName("label_Pname")
        self.gridLayout_6.addWidget(self.label_Pname, 0, 0, 1, 1)
        self.lineEdit_Pname = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_Pname.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Pname.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_Pname.setObjectName("lineEdit_Pname")
        self.lineEdit_Pname.setMaxLength(42)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.lineEdit_Pname.setFont(font)
        self.gridLayout_6.addWidget(self.lineEdit_Pname, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_Wname = QtWidgets.QLabel(self.frame_10)
        self.label_Wname.setMinimumSize(QtCore.QSize(170, 0))
        self.label_Wname.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_Wname.setFont(font)
        self.label_Wname.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_Wname.setObjectName("label_Wname")
        self.gridLayout_7.addWidget(self.label_Wname, 0, 0, 1, 1)
        self.lineEdit_Wname = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_Wname.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Wname.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_Wname.setObjectName("lineEdit_Wname")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.lineEdit_Wname.setFont(font)
        self.gridLayout_7.addWidget(self.lineEdit_Wname, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_5)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_JTitle = QtWidgets.QLabel(self.frame_11)
        self.label_JTitle.setMinimumSize(QtCore.QSize(170, 0))
        self.label_JTitle.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_JTitle.setFont(font)
        self.label_JTitle.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_JTitle.setObjectName("label_JTitle")
        self.gridLayout_8.addWidget(self.label_JTitle, 0, 0, 1, 1)
        self.lineEdit_Jtitle = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_Jtitle.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Jtitle.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_Jtitle.setObjectName("lineEdit_Jtitle")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.lineEdit_Jtitle.setFont(font)
        self.gridLayout_8.addWidget(self.lineEdit_Jtitle, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_5)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_Task = QtWidgets.QLabel(self.frame_12)
        self.label_Task.setMinimumSize(QtCore.QSize(170, 0))
        self.label_Task.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Task.setFont(font)
        self.label_Task.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_Task.setObjectName("label_Task")
        self.gridLayout_9.addWidget(self.label_Task, 0, 0, 1, 1)
        self.lineEdit_Task = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_Task.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_Task.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_Task.setObjectName("lineEdit_Task")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.lineEdit_Task.setFont(font)
        self.gridLayout_9.addWidget(self.lineEdit_Task, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_5)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_ACond = QtWidgets.QLabel(self.frame_13)
        self.label_ACond.setMinimumSize(QtCore.QSize(170, 0))
        self.label_ACond.setMaximumSize(QtCore.QSize(170, 105))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_ACond.setFont(font)
        self.label_ACond.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_ACond.setObjectName("label_ACond")
        self.gridLayout_10.addWidget(self.label_ACond, 0, 0, 1, 1)
        self.lineEdit_ACond = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_ACond.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_ACond.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_ACond.setObjectName("lineEdit_ACond")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.lineEdit_ACond.setFont(font)
        self.gridLayout_10.addWidget(self.lineEdit_ACond, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_5)
        self.frame_14.setMinimumSize(QtCore.QSize(0, 90))
        self.frame_14.setMaximumSize(QtCore.QSize(16777215, 90))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_WithoutP = CustomButton(parent=self.frame_14, start_color=QColor(0, 153, 211), end_color=QColor(52, 196, 251))
        self.pushButton_WithoutP.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_WithoutP.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_WithoutP.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_WithoutP.setFont(font)
        self.pushButton_WithoutP.setStyleSheet("background-color: rgb(0, 153, 211);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_WithoutP.setObjectName("pushButton_WithoutP")
        self.gridLayout_11.addWidget(self.pushButton_WithoutP, 0, 0, 1, 1)
        self.pushButton_Create = CustomButton(parent=self.frame_14, start_color=QColor(0, 153, 211), end_color=QColor(52, 196, 251))
        self.pushButton_Create.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Create.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_Create.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Create.setFont(font)
        self.pushButton_Create.setStyleSheet("QPushButton {\n"
"    /* Adjust border and background properties */\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 5; /* This will remove the default border */\n"
"    background-color: rgb(0, 153, 211);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Define hover state properties if needed */\n"
"    background-color: rgb(52, 196, 251);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Define pressed state properties if needed */\n"
"    background-color: rgb(4, 140, 191);\n"
"}\n"
"")
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.gridLayout_11.addWidget(self.pushButton_Create, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_14)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setMinimumSize(QtCore.QSize(40, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.line = QtWidgets.QFrame(self.frame_6)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_12.addWidget(self.line, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(800, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(800, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.frame_15 = QtWidgets.QFrame(self.frame_4)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_18.setMaximumSize(QtCore.QSize(40, 40))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_14.addWidget(self.frame_18, 0, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame_15)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_19)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_2 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(7, 52, 96);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_15.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.frame_19, 0, 1, 1, 1)
        self.gridLayout_13.addWidget(self.frame_15, 0, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.frame_4)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        font = QFont("Segoe UI", 10) 
        self.tableWidget = CustomTableWidget(self.frame_16)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(206, 214, 223))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout_16.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_16, 1, 0, 1, 1)
        self.frame_17 = QtWidgets.QFrame(self.frame_4)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 41))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setHorizontalSpacing(10)
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.pushButton_Refresh = CustomButton(self.frame_17)
        self.pushButton_Refresh.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Refresh.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Refresh.setFont(font)
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.gridLayout_17.addWidget(self.pushButton_Refresh, 0, 0, 1, 1)
        self.pushButton_Delete = CustomButton(parent=self.frame_17, start_color=QColor(31, 90, 146), end_color=QColor("#3a80c6"), pressed_color=QColor("#1a4876"))
        self.pushButton_Delete.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Delete.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Delete.setFont(font)
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.gridLayout_17.addWidget(self.pushButton_Delete, 0, 1, 1, 1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Open = CustomButton(parent=self.frame_17, start_color=QColor(0, 163, 26), end_color=QColor("#45bc58"), pressed_color=QColor("#469e54"))
        self.pushButton_Open.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_Open.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Open.setFont(font)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.gridLayout_17.addWidget(self.pushButton_Open, 0, 3, 1, 1)
        self.gridLayout_13.addWidget(self.frame_17, 2, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.cellClicked.connect(self.select_row)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  
        self.tableWidget.setSortingEnabled(True)
        self.pushButton_Delete.clicked.connect(self.delete_file)
        self.pushButton_WithoutP.clicked.connect(self.openCalculatorWithoutProject)
        self.pushButton_Open.clicked.connect(self.openProject)
        self.pushButton_Create.clicked.connect(self.createProject)
        self.tableWidget.itemSelectionChanged.connect(self.update_buttons)
        self.pushButton_Refresh.clicked.connect(self.loadData)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.cellDoubleClicked.connect(self.openProject)
        self.lineEdit_Task.setMaxLength(42)
        self.lineEdit_ACond.setMaxLength(42)
        self.lineEdit_Jtitle.setMaxLength(42)
        self.lineEdit_Wname.setMaxLength(42)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setStyleSheet("QTableWidget { background-color: #F0F0F0; }")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_buttons(self):
        if self.tableWidget.currentRow() == -1:
            self.pushButton_Delete.setEnabled(False)
            self.pushButton_Open.setEnabled(False)
        else:
            self.pushButton_Delete.setEnabled(True)
            self.pushButton_Open.setEnabled(True)

    def openCalculatorWithoutProject(self):
        self.TextsForData.set_ProjectN("None")
        self.TextsForData.set_A("None")
        self.openWindow()

    def createProject(self):
        if self.lineEdit_Pname.text() == "":
            error_msg = QMessageBox()
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setWindowTitle("Error")
            error_msg.setText(f"Please fill the project name.")
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.exec_()
        else:
            subfolder_name = self.lineEdit_Pname.text()
            parent_folder_path =os.path.join(file_path_to_HEC,subfolder_name)
            time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            # Check if the subfolder exists in the parent folder
            if not os.path.exists(parent_folder_path):
                os.makedirs(parent_folder_path)
                file_path = os.path.join(parent_folder_path, subfolder_name+"projectmain.txt")
                with open(file_path,"w") as file:
                    file.write("""{Project Details for """+subfolder_name+"""}\n
                    (Project Name) """+subfolder_name+"""\n
                    (Worker's name) """+self.lineEdit_Wname.text()+"""\n
                    (Worker's job title) """+self.lineEdit_Jtitle.text()+"""\n
                    (Task) """+self.lineEdit_Task.text()+"""\n
                    (Assesment Conductor) """+self.lineEdit_ACond.text()+"""\n
                    (Time) """+time_str)
                self.TextsForData.set_ProjectN(self.lineEdit_Pname.text())
                self.TextsForData.set_A("None")
                self.TextsForData.set_vP("None")
                self.openWindow()
            else:
                error_msg = QMessageBox()
                error_msg.setIcon(QMessageBox.Critical)
                error_msg.setWindowTitle("Error")
                error_msg.setText(f"A project with the name '{subfolder_name}' already exists.")
                error_msg.setStandardButtons(QMessageBox.Ok)
                error_msg.exec_()
            
    def openWindow(self):
        self.window = CustomMainWindow()
        self.ui = Ui_CalculateWindow(self.TextsForData)
        self.ui.setupUi(self.window)
        self.window.showMaximized()

    def openProject(self):
        listOfMainS = ["A", "B1", "B3", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "LL", "LP", "LQ","textactions", "vP"]
        row = self.tableWidget.currentRow()
        if row == -1:
            return
        subfolder_name = self.tableWidget.item(row, 0).text()
        parent_folder_path = os.path.join(file_path_to_HEC, subfolder_name)
        filename = os.path.join(parent_folder_path, subfolder_name + 'projectdetail.txt')
        values = {}
        pattern = re.compile(r'({}):([^\n]*)(?=\s|$)'.format('|'.join(listOfMainS)))

        multiline_keys = ["LL", "LP", "LQ", "textactions", "vP"]
        current_key = None
        if os.path.exists(filename): 
            with open(filename, "r") as file:
                lines = file.readlines()
                for line in lines[1:]:  # Skip the first line
                    if current_key in multiline_keys:
                        if line.strip() and not any(line.startswith(f"{key}:") for key in listOfMainS):
                            values[current_key] += "\n" + line.rstrip()
                        else:
                            current_key = None

                    match = pattern.search(line)
                    if match:
                        key = match.group(1)
                        value = match.group(2)
                        current_key = key
                        if key not in values:  # This condition is added to avoid overwriting existing values
                            values[key] = value.strip()
            self.TextsForData.set_ProjectN(subfolder_name)
            for key, value in values.items():
                if key == "B1" and value != "None":
                    self.TextsForData.set_B1(values["B1"])
                    self.TextsForData.set_B3("None")
                elif key == "B3" and value != "None":
                    self.TextsForData.set_B3(values["B3"])
                    self.TextsForData.set_B1("None")
                else:
                    method = getattr(self.TextsForData, f"set_{key}")
                    method(value)
        else:
            show_info_popup(f"For this project, the selections couldn't found.")
            self.TextsForData.set_A("None")
            self.TextsForData.set_vP("None")
            self.TextsForData.textactions = "None"
            self.TextsForData.set_ProjectN(subfolder_name)
            
        self.openWindow()

    def read_data(self):
        file_path_to_HEC = os.path.join(home_dir, "AppData/Local/HEC Calculator")
        if not os.path.exists(file_path_to_HEC):
            os.makedirs(file_path_to_HEC)
        def list_folders(path):
            folders = [entry.name for entry in os.scandir(path) if entry.is_dir()]
            return folders
        
        folder_list = list_folders(file_path_to_HEC)
        projects=[]
        listOfMainS=["Project Name","Worker's name","Worker's job title","Task","Assesment Conductor","Time"]
        for folder in folder_list:
            parent_folder_path =os.path.join(file_path_to_HEC,folder)
            
            if os.path.exists(parent_folder_path):
                file_path = os.path.join(parent_folder_path, folder+"projectmain.txt")
                with open(file_path,"r") as file:
                    content = file.read()
                    new_project = {"Project Name": None, "Worker's name": None, "Worker's job title": None, "Task": None, "Assesment Conductor": None,"Time": None}
                    for name in listOfMainS:
                        pattern = r"\("+name+"\)(.+)"
                        match = re.search(pattern, content, re.MULTILINE)
                        if match:
                            if match.group(1).strip():
                                new_project[name]=match.group(1).strip()
                    projects.append(new_project)
        return projects
        
    def loadDataToTable(self,projects):
        self.tableWidget.setRowCount(len(projects))
        row=0
        for project in projects:
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(project["Project Name"]))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(project["Worker's name"]))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(project["Worker's job title"]))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(project["Task"]))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(project["Assesment Conductor"]))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(project["Time"]))
            row+=1
    def loadData(self):
        projects = self.read_data()
        self.loadDataToTable(projects)

    def delete_file(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            return
    
        project_name = self.tableWidget.item(selected_row, 0).text()
    
        # Create a custom QMessageBox
        msg_box = QtWidgets.QMessageBox(self.centralwidget)
        msg_box.setWindowTitle("Delete Confirmation")
        msg_box.setText("Are you sure you want to delete this folder?")
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.setWindowFlag(Qt.NoDropShadowWindowHint)  # Disable the sound
    
        reply = msg_box.exec()
    
        home_dir = os.path.expanduser("~")
        file_path_to_HEC = os.path.join(home_dir, "AppData/Local/HEC Calculator")
        folder_path = os.path.join(file_path_to_HEC, project_name)
        if reply == QtWidgets.QMessageBox.Yes:
            try:
                shutil.rmtree(folder_path)
                self.tableWidget.removeRow(selected_row)
                QtWidgets.QMessageBox.information(
                    self.centralwidget,
                    "Success",
                    "Folder deleted successfully.",
                )
            except Exception as e:
                QtWidgets.QMessageBox.warning(
                    self.centralwidget,
                    "Error",
                    f"An error occurred while deleting the folder: {str(e)}",
                )
    
    def select_row(self, row, column):
        self.tableWidget.selectRow(row)
        project_name = self.tableWidget.item(row, 0).text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "New Project"))
        self.label_Pname.setText(_translate("MainWindow", "Project Name"))
        self.label_Wname.setText(_translate("MainWindow", "Worker\'s Name"))
        self.label_JTitle.setText(_translate("MainWindow", "Worker\'s Job Title"))
        self.label_Task.setText(_translate("MainWindow", "Task"))
        self.label_ACond.setText(_translate("MainWindow", "Assesment Conductor"))
        self.pushButton_WithoutP.setText(_translate("MainWindow", "Use Calculator without Project"))
        self.pushButton_Create.setText(_translate("MainWindow", "+ Create New Project"))
        self.label_2.setText(_translate("MainWindow", "Saved Projects"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Project\'s Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Worker\'s Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Worker's Job Title"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Task"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Conductor"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Time"))
        self.pushButton_Refresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_Delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open"))
        MainWindow.setStyleSheet("""
    QWidget {
        background-color: #F0F0F0;
    }

    /* Customize the scroll bar */
    QScrollBar:vertical {
        background: #f0f0f0;
        width: 15px;
        margin: 0;
    }

    QScrollBar::handle:vertical {
        background: #bacada;
        min-height: 20px;
    }

    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
        height: 0;
        subcontrol-origin: margin;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }

    QScrollBar:horizontal {
        background: #f0f0f0;
        height: 15px;
        margin: 0;
    }

    QScrollBar::handle:horizontal {
        background: #bacada;
        min-width: 20px;
    }

    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
        background: none;
        width: 0;
        subcontrol-origin: margin;
    }

    QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
        background: none;
    }

    QTableWidget QHeaderView::section {
        background-color: #F0F0F0;
        color: black;
        padding: 4px;
        font-weight: bold;
        border-right: 1px solid #D0D0D0;  /* Add a thin line between the column names */
        border-top: 1px solid #F0F0F0;
        border-bottom: 1px solid #F0F0F0;
    }

    QTableWidget QHeaderView::section:first {  /* Add this block to change the first column border */
        border-left: 1px solid #F0F0F0;
    }

    QTableWidget QTableCornerButton::section {  /* Add this block to change the corner button color */
        background-color: #F0F0F0;
        border: none;
        border-right: 1px solid #D0D0D0;  /* Add a thin line to the right */
        border-bottom: 1px solid #D0D0D0;  /* Add a thin line at the bottom */
    }
""")
        self.loadData()