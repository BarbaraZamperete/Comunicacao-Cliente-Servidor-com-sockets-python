# #######################Server.py###########################
# MULTITREADING

from socket import *
from threading import *



LOCALHOST = "127.0.0.1"
PORT = 8000
PACKET = 1024

class ClientThread(Thread):
    #Essa classe herda da classe Thread
    def __init__(self, clientAddress, clientsocket):
        Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão com: ", clientAddress)
        self.clientAddress = clientAddress

    def run(self):
        while True:
            data = self.csocket.recv(PACKET)
            dataFromClient = data.decode()
            # print("Recebido do cliente %s: %s" % (self.clientAddress, dataFromClient))
            # Inverte a String
            resposta = dataFromClient[::-1]
            self.csocket.send(bytes(resposta, 'UTF-8'))


s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((LOCALHOST, PORT))
print("Server Iniciado")
print("Waiting for client request..")
s.listen()
clientes = 0
while True:
    clientsock, clientAddress = s.accept()
    #iniciando uma thread com esse client
    newthread = ClientThread(clientAddress, clientsock) 
    clientes += 1
    print("Cliente: ", clientes)
    newthread.start()
