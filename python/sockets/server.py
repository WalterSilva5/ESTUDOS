import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ifnet = ipv4, sock_stream = tcpip
s.bind((socket.gethostbyname("23.1.1.250"),12397))
s.listen(5)
print("conectado")
while True:
    clientsocket, addres = s.accept()
    print(f"CONNECTION FROM {addres} has been established!")
    clientsocket.send(bytes("YOU ARE CONNECTED INTO THE SERVER!", "utf-8"))
    clientsocket.close()