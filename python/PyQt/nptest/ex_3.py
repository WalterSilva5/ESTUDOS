import sys
import socket
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QLabel,
    QLineEdit, QVBoxLayout
)
from PyQt6.QtCore import QThread, pyqtSignal
from time import sleep
import re


class DNSThread(QThread):
    result = pyqtSignal(str)

    def __init__(self, hostname):
        super().__init__()
        self.hostname = hostname

    def run(self):
        for i in range(10):
            try:
                ip = socket.gethostbyname(self.hostname)
                self.result.emit(f"Tentativa {i+1}: {self.hostname} resolvido como {ip}")
            except socket.gaierror:
                self.result.emit(f"Tentativa {i+1}: Falha ao resolver {self.hostname}")
            sleep(1)

class DNSCheckerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DNS Checker')
        self.resize(600, 500)

        self.layout = QVBoxLayout()

        self.hostname_label = QLabel('Hostname:')
        self.layout.addWidget(self.hostname_label)

        self.hostname_input = QLineEdit()
        self.layout.addWidget(self.hostname_input)

        self.check_button = QPushButton('Verificar DNS')
        self.check_button.clicked.connect(self.start_check)
        self.layout.addWidget(self.check_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def adapt_url(self, url: str) -> str:
        return re.sub(r'^https?:\/\/', '', url).split('/')[0]
    
    def start_check(self):
        hostname = self.hostname_input.text()
        self.dns_thread = DNSThread(self.adapt_url(hostname))
        self.dns_thread.result.connect(self.update_result)
        self.dns_thread.start()

    def update_result(self, message):
        self.result_label.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DNSCheckerApp()
    window.show()
    sys.exit(app.exec())
