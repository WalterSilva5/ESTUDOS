from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from src.screen.main_window.view.main_window_view import Ui_main_window as Ui_MainWindow
import random, threading, time
from datetime import datetime


from PyQt5.QtWidgets import QStackedWidget
from src.screen.home_screen.view.home_screen_view import Ui_home_window as Ui_HomeScreen

class MainWindowController(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model

        # Stacked widget to manage different screens
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Login screen setup
        self.login_screen = Ui_MainWindow()
        self.login_widget = QWidget()
        self.login_screen.setupUi(self.login_widget)
        self.stacked_widget.addWidget(self.login_widget)
        
        # Home screen setup
        self.home_screen = Ui_HomeScreen()
        self.home_widget = QWidget()
        self.home_screen.setupUi(self.home_widget)
        self.stacked_widget.addWidget(self.home_widget)

        # Initially show login screen
        self.stacked_widget.setCurrentWidget(self.login_widget)

        self.login_screen.login_submit_button.clicked.connect(self.exibirConteudo)

    def exibirConteudo(self):
        login = self.login_screen.login_input.toPlainText()
        password = self.login_screen.password_input.toPlainText()

        # Sample check for now. In a real-world scenario, this would be real authentication.
        if login and password:
            self.stacked_widget.setCurrentWidget(self.home_widget)
