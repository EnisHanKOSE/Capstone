import sys

from PyQt5 import QtWidgets
from CreatePage import Ui_CreatePage
from installApps import check_and_install_programs
from TextsForData import Texts

TextsForData = Texts()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_CreatePage(TextsForData)
    ui.setupUi(MainWindow)
    MainWindow.show()
    check_and_install_programs()

    sys.exit(app.exec_())
    