import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QProgressBar
)
from PyQt6.QtCore import QThread, pyqtSignal
import wget

class DownloadThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        def bar_progress(current, total, width=80):
            progress = int((current / total) * 100)
            self.progress.emit(progress)

        wget.download(self.url, bar=bar_progress)

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sample Downloader')
        self.resize(600, 100)

        self.layout = QVBoxLayout()

        self.url_label = QLabel('URL:')
        self.layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        self.layout.addWidget(self.url_input)

        self.download_button = QPushButton('Download')
        self.download_button.clicked.connect(self.start_download)
        self.layout.addWidget(self.download_button)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.setLayout(self.layout)

    def start_download(self):
        self.url = self.url_input.text()
        self.download_thread = DownloadThread(self.url)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.start()

    def update_progress(self, value):
        self.progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec())
