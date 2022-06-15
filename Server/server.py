import threading
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conectando o Servidor
    try:
        server.bind(('localhost', 7777))
        server.listen() # ouvindo conecções
    except:
        return print('\nNão foi possivel iniciar o Servidor!\n')

    while True: # aceitando conecções
         client, addr = server.accept()
         clients.append(client) # adicionando client a lista

         thread = threading.Thread(target=messagesTreatment, args=[client])
         thread.start()

    # Tratando as menssagens / recebe a menssagem e envia para os clients
def messagesTreatment(client):
    while True:
        try:
            message = client.recv(2048)
            broadcast(message, client)
        except:
            deleteClient(client)
            break

    # Transmite as menssagens ate os clientes
def broadcast(message, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(message)
            except:
                deleteClient(clientItem)

    # Deletar cliente
def deleteClient(client):
    clients.remove(client)

main()