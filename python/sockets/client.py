"""import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname("23.1.1.250"),12397))

msg = s.recv(1024)
print(msg.decode("utf-8"))"""

from tkinter import *

window = Tk()
window.title("ALERTA FRINPE")
window.geometry("800x600")
window.mainloop()