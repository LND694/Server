import socket
import threading

port = 5050
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER , port)
server.bind((ADDR))
FORMAT = 'utf-8'
DISCONNECT_MSG = '!Disconnect'

conns = []
nicknames = []


def broadcast(message):
    for conn in conns:
        conn.send(message)

def hande_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} is  Connected")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length=  int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                broadcast(msg)
                if msg == DISCONNECT_MSG:
                    connected = False
            print(f"[{addr}] {msg}")
            conn.close()
        except:
            index = conns.index(conn)
            conns.remove(conn)
            conn.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
 


def start(): #Starts the server itself and listening to connections
    server.listen()
    while True:
        conn, addr = server.accept()
        conn.send('NICKNAME'.encode(FORMAT))
        nickname = conn.recv(HEADER).decode(FORMAT)
        nicknames.append(nickname)
        conns.append(conn)
        print(f'[SERVER] {nickname} is connected')
        broadcast(f'{nickname} joined the chat'.encode(FORMAT))
        conn.send('Coneected to the server')

        thread= threading.Thread(target=hande_client, args=(conn, addr))
        thread.start
        print(f"[ACTIVE CONNECTIONS]: {threading.active_count}")



print("[SERVER] server is starting...")
start()
    


