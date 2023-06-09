from PyQt5.QtWidgets import QMessageBox

def show_info_popup(message):
    info_msg = QMessageBox()
    info_msg.setIcon(QMessageBox.Information)
    info_msg.setWindowTitle("Information")
    info_msg.setText(message)
    info_msg.setStandardButtons(QMessageBox.Ok)
    info_msg.exec_()
def show_popup():
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Check the B section")
        x= msg.exec_()