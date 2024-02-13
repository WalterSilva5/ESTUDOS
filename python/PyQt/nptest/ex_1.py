import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QLabel)
from datetime import datetime


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt6 App ex1')

window.resize(600, 500)

bt_label = QLabel("CONFIRMAR", window)
bt_label.move(100, 200)

def fun_test():
    bt_label.setText(f"click event at: {datetime.now()}")
    bt_label.adjustSize()

ok_button = QPushButton("OK", window)
ok_button.setGeometry(200, 100, 100, 50)
ok_button.setStyleSheet("background-color: red;")
ok_button.clicked.connect(fun_test)

if __name__ == "__main__":
    window.show()
    app.exec()