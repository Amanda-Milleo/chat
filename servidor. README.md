Servidor 

import socket
import threading

HOST = '192.168.1.4'
PORT = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST E PORTA
sock.bind((HOST,PORT))

#SERVER ESCUTA
sock.listen()
print(f"O servidor {HOST}:{PORT} está aguardando conexões")


names = {
    }

def RecebeDados(conn, ender):
    try:
        nome = conn.recv(1024).decode()
        names[conn] = nome
        for cliente in names:
                if cliente != conn:
                    cliente.sendall(str.encode(f"'{names[conn]}' se conectou"))
    except:
        print("Ocorreu um erro durante o recebimento do nome de um novo usuário")
        return
    print(f"Conectado com {nome}, IP: {ender[0]}, PORTA: {ender[1]}")
    while True:
        try:
            mensagem = conn.recv(1024).decode()
            ver = True

            if mensagem == "666":
                break
            for cliente in names:
                sub = "@" + names[cliente]
                if sub in mensagem:
                    cliente.sendall(str.encode(f"{names[cliente]}: {mensagem}"))
                    ver = False
            print(f"{nome} >> {mensagem}")
            if ver:
                for cliente in names:
                    if cliente != conn:
                        cliente.sendall(str.encode(f"{names[conn]}: {mensagem}"))
            
        except:
            print("Ocorreu algum erro na recepção de dados, encerrando conexão")
            break
        
        toSendMsg = (f"{nome} >> {mensagem}")
        print(toSendMsg)
    conn.close()
    
while True:

    #CRIANDO A CONEÇÃO
    try:
        conn,ender = sock.accept()
    except:
        print("Ocorreu um erro durante o ACCEPT() de um novo usuário")
        continue
    
    threadRecebeDados = threading.Thread(target = RecebeDados, args = ([conn,ender]))
    threadRecebeDados.start()
 

