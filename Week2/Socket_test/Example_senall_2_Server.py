import socket
import sys

HOST = None
PORT = 50007
s = None

for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af,socktype,proto,canonname,sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not ope socket')
    sys.exit(1)
conn,addr = s.accept()
with conn:
    print('coneccted by',addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)