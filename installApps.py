import urllib.request, subprocess, os
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QMessageBox, QProgressDialog, QApplication
from Popups import show_info_popup
from queue import Queue

class InstallProgramThread(QThread):
    error = pyqtSignal(str)
    progress = pyqtSignal(int)
    success = pyqtSignal(str)

    def __init__(self, installers_queue):
        super().__init__()
        self.installers_queue = installers_queue

    def run(self):
        while not self.installers_queue.empty():
            installer = self.installers_queue.get()
            try:
                subprocess.run([installer["installer_path"]] + installer.get("install_arguments", ["/verysilent", "/norestart"]), shell=True, check=True)
                self.success.emit(installer["program_name"])
            except Exception as e:
                self.error.emit(f"An error occurred while installing {installer['program_name']}: {str(e)}")
                return
            self.progress.emit(100)
            self.installers_queue.task_done()
def is_klite_installed():
    codec_tweak_tool = 'CodecTweakTool.exe'
    search_directories = [
        os.path.join(os.environ['ProgramFiles'], 'K-Lite Codec Pack'),
        os.path.join(os.environ['ProgramFiles(x86)'], 'K-Lite Codec Pack'),
    ]

    for search_directory in search_directories:
        for root, _, files in os.walk(search_directory):
            if codec_tweak_tool in files:
                return True

    return False
def is_tesseract_installed():
    tesseract_exe = 'tesseract.exe'
    search_directories = [
        os.path.join(os.environ['ProgramFiles'], 'Tesseract-OCR'),
        os.path.join(os.environ['ProgramFiles(x86)'], 'Tesseract-OCR'),
    ]

    for search_directory in search_directories:
        for root, _, files in os.walk(search_directory):
            if tesseract_exe in files:
                return True

    return False
def check_and_install_programs(parent=None):
    installers = [
        {
            "check_func": is_klite_installed,
            "installer_path": os.path.join("resources", "K-Lite_Codec_Pack_1755_Basic.exe"),
            "program_name": "K-Lite Codec Pack",
        },
        {
            "check_func": is_tesseract_installed,
            "installer_path": os.path.join("resources", "tesseract-ocr-w64-setup-5.3.1.20230401.exe"),
            "program_name": "Tesseract OCR",
            "install_arguments": ["/S"],
        }

    ]

    installers_queue = Queue()
    for installer in installers:
        if not installer["check_func"]():
            user_response = QMessageBox.question(parent, f"{installer['program_name']} not installed",
                                                 f"{installer['program_name']} is not installed. Do you want to install it?",
                                                 QMessageBox.Yes | QMessageBox.No)

            if user_response == QMessageBox.Yes:
                installers_queue.put(installer)

    if not installers_queue.empty():
        progress_dialog = QProgressDialog("Installing...",
                                          "Cancel", 0, 100, parent)
        progress_dialog.setWindowModality(Qt.ApplicationModal)
        progress_dialog.setAutoClose(False)
        progress_dialog.setAutoReset(False)
        progress_dialog.setValue(0)
        progress_dialog.show()

        install_thread = InstallProgramThread(installers_queue)
        install_thread.error.connect(show_info_popup)
        install_thread.progress.connect(progress_dialog.setValue)
        install_thread.success.connect(lambda name: QMessageBox.information(parent, "Installation completed",
                                        f"{name} has been successfully installed."))
        install_thread.finished.connect(progress_dialog.close)
        install_thread.start()

        QApplication.processEvents()
