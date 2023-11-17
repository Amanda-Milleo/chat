import socket
import threading

HOST = '192.168.1.4'
PORT = 55555

#AF_INET é IPv4
#SOCK_STREAM é TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST,PORT))

# Nome
nome = input("Digite seu nome: ")
sock.sendall(str.encode(nome))
print(f"{nome} entrou no chat")

def RecebeDados(sock):
    while True:
        try:
            mensagemR = sock.recv(1024).decode()
            print(" ")
            print(mensagemR)
            print('Digite sua mensagem (digite "666" para sair): ')
        except:
           break 
        


# Mensagem cliente
try:
    threadRecebeDados = threading.Thread(target = RecebeDados, args = ([sock]))
    threadRecebeDados.start()
    while True:
        mensagem = input('Digite sua mensagem (digite "666" para sair): ')
        if mensagem == "666":
            print(f"{nome} saiu")
            break
        sock.sendall(str.encode(mensagem))
        
finally:
    sock.close()


