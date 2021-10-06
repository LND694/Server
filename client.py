import socket

SREVER = "192.168.1.179"
PORT = 5050
ADDR= (SREVER, PORT)
DISCONNECT_MSG= "!Disconnect"
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDR))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenght = str(msg_length).encode(FORMAT) 