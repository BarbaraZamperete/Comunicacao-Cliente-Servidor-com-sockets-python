#######################Client.py###########################

from socket import *

SERVER = "127.0.0.1"
PORT = 8000

c = socket(AF_INET, SOCK_STREAM)

c.connect((SERVER, PORT))

print("Qual mensagem deseja enviar?")
# dataClient = input()

dataClient = "Hello World!!!"
c.sendall(bytes(dataClient, 'UTF-8'))
while True:
    
    serverData = c.recv(1024)
    print("Resposta do Servidor:", serverData.decode())
    # dataClient = input()
    c.sendall(bytes(dataClient, 'UTF-8'))
    if dataClient == 'bye':
        break
c.close()
