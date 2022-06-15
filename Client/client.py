import threading
import socket

def main():
        # IPV4 Protocolo TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Cenectando o Servidor
    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possivel encontrar o Servidor!\n')

    name = input('Usuário::')
    print('\nUsuario Conectado')

        # Criando as threads para que as fubções rodem ao mesmo tempo
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, name])

        # Executando as threads
    thread1.start()
    thread2.start()

    # função para Receber Menssagens
def receiveMessages(client):

    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            print(message+'\n')
        except:
            print('\nUsuario desconectado do Servidor!\n')
            print('Pressione <Enter> para Continuar...')
            client.close()
            break

    # função para Enviar Menssagens
def sendMessages(client, name):
    
    while True:
        try:
            message = input('\n')
                # Envia em bit
            client.send(f'<{name}> {message}'.encode('utf-8'))
        except:
            return

main()