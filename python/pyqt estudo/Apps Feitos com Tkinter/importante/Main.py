from tkinter import *
from Frame import *

class root(Tk):
    def __init__(self):
        super().__init__(self)
        self.geometry("800x600+100+100")
        self.title("Programa de testes")
        self.frame = Application()
        self.mainloop()

app = root()
