import urllib.request, subprocess, os
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QMessageBox, QProgressDialog, QApplication
from Popups import show_info_popup

class DownloadAndInstallKLiteThread(QThread):
    error = pyqtSignal(str)
    progress = pyqtSignal(int)
    success = pyqtSignal()

    def __init__(self, link, installer_path):
        super().__init__()
        self.link = link
        self.installer_path = installer_path

    def run(self):
        try:
            with urllib.request.urlopen(self.link) as response, open(self.installer_path, 'wb') as out_file:
                self.progress.emit(50)
                out_file.write(response.read())
        except Exception as e:
            self.error.emit(f"An error occurred while downloading K-Lite Codec Pack: {str(e)}")
            return

        try:
            subprocess.run([self.installer_path, "/verysilent", "/norestart"], check=True)
        except Exception as e:
            self.error.emit(f"An error occurred while installing K-Lite Codec Pack: {str(e)}")
            return

        self.progress.emit(100)
        self.success.emit()

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
def check_and_install_klite(parent=None):
    if not is_klite_installed():
        link = "https://files3.codecguide.com/K-Lite_Codec_Pack_1755_Basic.exe"
        installer_path = os.path.join(os.path.expanduser("~"), "Downloads", "K-Lite_Codec_Pack_1745_Basic.exe")
        
        user_response = QMessageBox.question(parent, "K-Lite Codec Pack not installed",
                                             "K-Lite Codec Pack is not installed. Do you want to download and install it?",
                                             QMessageBox.Yes | QMessageBox.No)

        if user_response == QMessageBox.Yes:
            progress_dialog = QProgressDialog("Downloading and installing K-Lite Codec Pack...",
                                              "Cancel", 0, 100, parent)
            progress_dialog.setWindowModality(Qt.ApplicationModal)
            progress_dialog.setAutoClose(False)
            progress_dialog.setAutoReset(False)
            progress_dialog.setValue(0)
            progress_dialog.show()

            download_install_thread = DownloadAndInstallKLiteThread(link, installer_path)
            download_install_thread.error.connect(show_info_popup)
            download_install_thread.progress.connect(progress_dialog.setValue)
            download_install_thread.finished.connect(progress_dialog.close)
            download_install_thread.success.connect(lambda: QMessageBox.information(parent, "Installation completed",
                                            "K-Lite Codec Pack has been successfully downloaded and installed."))
            download_install_thread.start()

            QApplication.processEvents()
