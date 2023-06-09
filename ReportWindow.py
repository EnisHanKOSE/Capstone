import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QDialog,QVBoxLayout,QLabel,QFileDialog
from PyQt5.QtGui import QColor,QPixmap

from CustomPyQt import CustomButton
from Functions import (CreateFilePath, CalculateBackB1, CalculateBackB3, CalculateDriving
, CalculateNeck, CalculateShoulderArm, CalculateStress, CalculateVibration, CalculateWristHand, 
CalculateWorkPace)

home_dir, file_path_to_HEC =CreateFilePath()

class Ui_ReportWindow(object):
    def __init__(self, TextsForData):
        self.TextsForData = TextsForData
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 700)
        MainWindow.setMinimumSize(QtCore.QSize(740, 700))
        MainWindow.setMaximumSize(QtCore.QSize(740, 700))
        MainWindow.setStyleSheet("""
    QWidget {
        background-color: #F0F0F0;
    }
""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 90, 148);")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 350))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 350))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(25, 10, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(226, 3, 3);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 169, 3);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(255, 169, 3);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(34, -1, 34, -1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 7, -1, 7)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    /* Adjust border and background properties */\n"
"    border: none; /* This will remove the default border */\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon__info_empty_ (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setMinimumSize(QtCore.QSize(126, 0))
        self.label_10.setMaximumSize(QtCore.QSize(126, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setMinimumSize(QtCore.QSize(26, 26))
        self.frame_7.setMaximumSize(QtCore.QSize(26, 26))
        self.frame_7.setStyleSheet("background-color: rgb(255, 215, 5);\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout.addWidget(self.frame_7)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setMinimumSize(QtCore.QSize(90, 0))
        self.label_11.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setMinimumSize(QtCore.QSize(26, 26))
        self.frame_8.setMaximumSize(QtCore.QSize(26, 26))
        self.frame_8.setStyleSheet("background-color: rgb(255, 169, 3);\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout.addWidget(self.frame_8)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setMinimumSize(QtCore.QSize(90, 0))
        self.label_12.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.frame_10 = QtWidgets.QFrame(self.frame_3)
        self.frame_10.setMinimumSize(QtCore.QSize(26, 26))
        self.frame_10.setMaximumSize(QtCore.QSize(26, 26))
        self.frame_10.setStyleSheet("background-color: rgb(226, 3, 3);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout.addWidget(self.frame_10)
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setMinimumSize(QtCore.QSize(90, 0))
        self.label_14.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.frame_9 = QtWidgets.QFrame(self.frame_3)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 26))
        self.frame_9.setMaximumSize(QtCore.QSize(26, 26))
        self.frame_9.setStyleSheet("background-color: rgb(133, 13, 13);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout.addWidget(self.frame_9)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setMinimumSize(QtCore.QSize(90, 0))
        self.label_13.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(34, 0, 34, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(8, 52, 96);")
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setContentsMargins(34, -1, 34, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit.setObjectName("textEdit")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Segoe UI")
        self.textEdit.setFont(font)
        self.gridLayout_5.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(34, 10, 34, 10)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel = CustomButton(parent=self.frame_6, start_color=QColor(121, 156, 191), end_color=QColor(156,188,220), pressed_color=QColor(88,133,177))
        self.cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.cancel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_2.addWidget(self.cancel)
        self.export = CustomButton(parent=self.frame_6, start_color=QColor(121, 156, 191), end_color=QColor(156,188,220), pressed_color=QColor(88,133,177))
        self.export.setMinimumSize(QtCore.QSize(0, 50))
        self.export.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.export.setFont(font)
        self.export.setObjectName("export")
        self.horizontalLayout_2.addWidget(self.export)
        self.saveButton = CustomButton(parent=self.frame_6, start_color=QColor(31, 90, 148), end_color=QColor(58,128,198), pressed_color=QColor(26,72,118))
        self.saveButton.setMinimumSize(QtCore.QSize(0, 50))
        self.saveButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.update_save_button_state()
        self.saveButton.clicked.connect(self.saveProject)
        self.cancel.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.open_image)
    def closeEvent(self, event):
        self.close()
    def update_save_button_state(self):
        if self.TextsForData.get_ProjectN() == "None":
            self.saveButton.setEnabled(False)
        else:
            self.saveButton.setEnabled(True)
    def saveProject(self):
        subfolder_name = self.TextsForData.get_ProjectN()
        parent_folder_path = os.path.join(file_path_to_HEC, subfolder_name)
        file_path = os.path.join(parent_folder_path, f"{subfolder_name}projectdetail.txt")
        if os.path.exists(file_path):
            msg_box = QMessageBox()
            msg_box.setWindowTitle('File Already Exists')
            msg_box.setText(f"The file '{subfolder_name}' already exists. Do you want to overwrite it?")
            msg_box.setIcon(QMessageBox.Question)
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.No:
                return
        elif not os.path.exists(parent_folder_path):
            os.makedirs(parent_folder_path)
        with open(file_path, "w") as file:
            self.TextsForData.set_textactions(self.textEdit.toPlainText())
            project_details = [
                f"Project Selections for {self.TextsForData.get_ProjectN()}",
                f"A: {self.TextsForData.get_A()}",
                f"B1: {self.TextsForData.get_B1()}",
                f"B3: {self.TextsForData.get_B3()}",
                f"C: {self.TextsForData.get_C()}",
                f"D: {self.TextsForData.get_D()}",
                f"E: {self.TextsForData.get_E()}",
                f"F: {self.TextsForData.get_F()}",
                f"G: {self.TextsForData.get_G()}",
                f"H: {self.TextsForData.get_H()}",
                f"J: {self.TextsForData.get_J()}",
                f"K: {self.TextsForData.get_K()}",
                f"L: {self.TextsForData.get_L()}",
                f"M: {self.TextsForData.get_M()}",
                f"N: {self.TextsForData.get_N()}",
                f"P: {self.TextsForData.get_P()}",
                f"Q: {self.TextsForData.get_Q()}",
                f"LL: {self.TextsForData.get_LL()}",
                f"LP: {self.TextsForData.get_LP()}",
                f"LQ: {self.TextsForData.get_LQ()}",
                f"textactions: {self.TextsForData.get_textactions()}",
                f"vP: {self.TextsForData.get_vP()}"
            ]
            file.write('\n'.join(project_details))
        msg = QMessageBox()
        msg.setWindowTitle("Project Saved")
        msg.setText(f"Project '{subfolder_name}' saved successfully.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    def open_image(self):
        image_dialog = QDialog(self.pushButton)
        image_dialog.setWindowTitle("Image")
        image_dialog.setFixedSize(619, 371)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        image_label = QLabel()
        pixmap = QPixmap("resources/Group_46.png")  # Replace with your image path
        pixmap = pixmap.scaled(619, 371)  # Adjust the size as needed
        image_label.setPixmap(pixmap)

        layout.addWidget(image_label)
        image_dialog.setLayout(layout)
        image_dialog.exec_()


    def setScoresColors(self):
        _translate = QtCore.QCoreApplication.translate
        if self.TextsForData.get_B3()==None:
            valueB1=CalculateBackB1(self.TextsForData.get_A(),self.TextsForData.get_B1(),self.TextsForData.get_H(),self.TextsForData.get_J())
            if 7<valueB1<16:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(255, 215, 5);
                    color: rgb(98,98,98);  /* White text */
                }
            """)
            elif 15<valueB1<23:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(255, 169, 3);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            elif 22<valueB1<30:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(226, 3, 3);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            elif 29<valueB1<41:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(133, 13, 13);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            self.label_2.setText(_translate("MainWindow", "  Back:                                                                                                     "+str(valueB1)))
        else:
            valueB3=CalculateBackB3(self.TextsForData.get_A(),self.TextsForData.get_B3(),self.TextsForData.get_H(),self.TextsForData.get_J())
            if 9<valueB3<21:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(255, 215, 5);
                    color: rgb(98,98,98);  /* White text */
                }
            """)
            elif 20<valueB3<31:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(255, 169, 3);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            elif 30<valueB3<41:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(226, 3, 3);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            elif 40<valueB3<57:
                self.label_2.setStyleSheet("""
                QLabel {
                    background-color: rgb(133, 13, 13);
                    color: rgb(255, 255, 255);  /* White text */
                }
            """)
            self.label_2.setText(_translate("MainWindow", "  Back:                                                                                                     "+str(valueB3)))
        valueShoulder=CalculateShoulderArm(self.TextsForData.get_C(),self.TextsForData.get_D(),self.TextsForData.get_H(),self.TextsForData.get_J())
        if 9<valueShoulder<21:
            self.label_3.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif 20<valueShoulder<31:
            self.label_3.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 30<valueShoulder<41:
            self.label_3.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 40<valueShoulder<57:
            self.label_3.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueWrist=CalculateWristHand(self.TextsForData.get_E(),self.TextsForData.get_F(),self.TextsForData.get_K(),self.TextsForData.get_J())
        if 9<valueWrist<21:
            self.label_4.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif 20<valueWrist<31:
            self.label_4.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 30<valueWrist<41:
            self.label_4.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 40<valueWrist<57:
            self.label_4.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueNeck=CalculateNeck(self.TextsForData.get_G(),self.TextsForData.get_J(),self.TextsForData.get_L())
        if 3<valueNeck<7:
            self.label_5.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif 7<valueNeck<11:
            self.label_5.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 11<valueNeck<15:
            self.label_5.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif 15<valueNeck<19:
            self.label_5.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueDriving=CalculateDriving(self.TextsForData.get_M())
        if valueDriving==1:
            self.label_6.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif valueDriving==4:
            self.label_6.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueDriving==9:
            self.label_6.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueDriving==16:
            self.label_6.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueVibration=CalculateVibration(self.TextsForData.get_N())
        if valueVibration==1:
            self.label_7.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif valueVibration==4:
            self.label_7.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueVibration==9:
            self.label_7.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueVibration==16:
            self.label_7.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueWorkpace=CalculateWorkPace(self.TextsForData.get_P())
        if valueWorkpace==1:
            self.label_8.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif valueWorkpace==4:
            self.label_8.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueWorkpace==9:
            self.label_8.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueWorkpace==16:
            self.label_8.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        valueStress=CalculateStress(self.TextsForData.get_Q())
        if valueStress==1:
            self.label_9.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 215, 5);
                color: rgb(98,98,98);  /* White text */
            }
        """)
        elif valueStress==4:
            self.label_9.setStyleSheet("""
            QLabel {
                background-color: rgb(255, 169, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueStress==9:
            self.label_9.setStyleSheet("""
            QLabel {
                background-color: rgb(226, 3, 3);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        elif valueStress==16:
            self.label_9.setStyleSheet("""
            QLabel {
                background-color: rgb(133, 13, 13);
                color: rgb(255, 255, 255);  /* White text */
            }
        """)
        self.label_3.setText(_translate("MainWindow", "  Shoulder/Arm:                                                                                     "+str(valueShoulder)))
        self.label_4.setText(_translate("MainWindow", "  Wrist/Hand:                                                                                         "+str(valueWrist)))
        self.label_5.setText(_translate("MainWindow", "  Neck:                                                                                                     "+str(valueNeck)))
        self.label_6.setText(_translate("MainWindow", "  Driving:                                                                                                  "+str(valueDriving)))
        self.label_7.setText(_translate("MainWindow", "  Vibration:                                                                                               "+str(valueVibration)))
        self.label_8.setText(_translate("MainWindow", "  Work pace:                                                                                            "+str(valueWorkpace)))
        self.label_9.setText(_translate("MainWindow", "  Stress:                                                                                                    "+str(valueStress)))
        if self.TextsForData.get_textactions()==None:
            self.textEdit.insertPlainText("")
        else:
            self.textEdit.insertPlainText(self.TextsForData.get_textactions())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "      Total Score"))
        self.setScoresColors()
        self.label_10.setText(_translate("MainWindow", "Exposure Level         "))
        self.label_11.setText(_translate("MainWindow", "Low"))
        self.label_12.setText(_translate("MainWindow", "Moderate"))
        self.label_14.setText(_translate("MainWindow", "High"))
        self.label_13.setText(_translate("MainWindow", "Very High"))
        self.label_15.setText(_translate("MainWindow", "Actions required:"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.export.setText(_translate("MainWindow", "Export"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.saveButton.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.export.setDisabled(True)