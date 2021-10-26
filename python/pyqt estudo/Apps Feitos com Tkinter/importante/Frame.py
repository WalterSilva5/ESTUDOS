from tkinter import *
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.msg = Label(self)
        self.msg["text"] = "ola"

    def say_hi(self):
        print("hi there, everyone!")

