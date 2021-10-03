# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.entrada = QtWidgets.QTextEdit(self.centralwidget)
        self.entrada.setGeometry(QtCore.QRect(20, 10, 731, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.entrada.setFont(font)
        self.entrada.setObjectName("entrada")
        self.mostrar = QtWidgets.QToolButton(self.centralwidget)
        self.mostrar.setGeometry(QtCore.QRect(290, 90, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.mostrar.setFont(font)
        self.mostrar.setObjectName("mostrar")
        self.saida = QtWidgets.QLabel(self.centralwidget)
        self.saida.setGeometry(QtCore.QRect(90, 240, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.saida.setFont(font)
        self.saida.setObjectName("saida")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mostrar.setText(_translate("MainWindow", "mostrar"))
        self.saida.setText(_translate("MainWindow", "saida"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
