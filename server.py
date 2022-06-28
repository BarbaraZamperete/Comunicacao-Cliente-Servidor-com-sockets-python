# #######################Server.py###########################
# MULTITREADING

from socket import *
from threading import *

class ClientThread(Thread):
    #Essa classe herda da classe Thread
    def __init__(self, clientAddress, clientsocket):
        Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão com: ", clientAddress)
        self.clientAddress = clientAddress

    def run(self):
        while True:
            data = self.csocket.recv(2048)
            dataFromClient = data.decode()
            if dataFromClient == 'bye':
                break
            print("Recebido do cliente %s: %s" % (self.clientAddress, dataFromClient))
            # Inverte a String
            resposta = dataFromClient[::-1]
            self.csocket.send(bytes(resposta, 'UTF-8'))
        print("Client at ", clientAddress, " disconnected...")


LOCALHOST = "127.0.0.1"
PORT = 8000
s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((LOCALHOST, PORT))
print("Server Iniciado")
print("Waiting for client request..")
while True:
    s.listen()
    clientsock, clientAddress = s.accept()
    #iniciando uma thread com esse client
    newthread = ClientThread(clientAddress, clientsock) 
    newthread.start()
