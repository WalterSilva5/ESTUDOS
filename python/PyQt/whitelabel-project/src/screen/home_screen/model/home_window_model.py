from PyQt5.QtCore import QObject
class MainWindowModel(QObject): 
    error_message = ""
    
    @property
    def error_message(self):
        return self.error_message

    @error_message.setter
    def error_message(self, mensagem):
        self.error_message = mensagem
        