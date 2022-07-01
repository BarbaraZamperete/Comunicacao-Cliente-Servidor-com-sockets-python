from socket import socket


from socket import *
import threading

SERVER = "127.0.0.1"
PORT = 8000
PACKET_SIZE = 1024

num = 0

def message():
    while True:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((SERVER, PORT))
            # dataClient = "Hello World!!!"
            # s.sendall(bytes(dataClient, 'UTF-8'))
            s.send("\x00")
            global num
            num += 1
            print(num)
        except error:
            print(error.errno)
        s.close()

for i in range(500):
    thread = threading.Thread(target=message)
    print("############ %d #########" % i)
    thread.start()