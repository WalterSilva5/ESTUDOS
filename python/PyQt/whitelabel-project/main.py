from src.screen.main_window.model.main_window_model import MainWindowModel
from src.screen.main_window.controller.main_window_controller import MainWindowController
from PyQt5.QtWidgets import QApplication

import sys

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = MainWindowModel()
        self.view = MainWindowController(self.model)
        self.view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec())