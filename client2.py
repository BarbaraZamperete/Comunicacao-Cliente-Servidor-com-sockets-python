#######################Client.py###########################

from socket import *
from threading import Thread

SERVER = "127.0.0.1"
PORT = 8000

c = socket(AF_INET, SOCK_STREAM)

c.connect((SERVER, PORT))

# print("Qual mensagem deseja enviar?")
# dataClient = input()

dataClient = "Hello World!!!"
c.sendall(bytes(dataClient, 'UTF-8'))
while True:
    
    serverData = c.recv(2048)
    print("Resposta do Servidor:", serverData.decode())
    # dataClient = input()
    c.sendall(bytes(dataClient, 'UTF-8'))
    if dataClient == 'bye':
        break
c.close()
