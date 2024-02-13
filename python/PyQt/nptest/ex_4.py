import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QStackedWidget


class LoginPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        layout.addWidget(self.username)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password)

        self.login_button = QPushButton("Login")
        layout.addWidget(self.login_button)

        self.setLayout(layout)
        

class MainPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()

        self.logout_button = QPushButton("Logout")
        layout.addWidget(self.logout_button)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt App with Login")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_panel = LoginPanel()
        self.main_panel = MainPanel()

        self.stacked_widget.addWidget(self.login_panel)
        self.stacked_widget.addWidget(self.main_panel)

        self.login_panel.login_button.clicked.connect(self.check_login)
        self.main_panel.logout_button.clicked.connect(self.logout)

    def check_login(self):
        self.stacked_widget.setCurrentWidget(self.main_panel)

    def logout(self):
        self.stacked_widget.setCurrentWidget(self.login_panel)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
