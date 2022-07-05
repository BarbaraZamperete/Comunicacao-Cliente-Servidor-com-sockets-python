from socket import socket


from socket import *
import threading

SERVER = "127.0.0.1"
PORT = 8000
PACKET = 1024

num = 0

def message():
    while True:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((SERVER, PORT))
            dataClient = "Hello World!!!"
            s.sendall(bytes(dataClient, 'UTF-8'))
            resposta = s.recv(PACKET)
            global num
            num += 1
            print("%d -> Resposta: %s" % (num, resposta.decode()))
        except error:
            print(error.errno)
            break
        s.close()

for i in range(100):
    thread = threading.Thread(target=message)
    thread.start()