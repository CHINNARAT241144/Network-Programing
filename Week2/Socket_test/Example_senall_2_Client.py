import socket
import sys

HOST = 'localhost'
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
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could noty open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hello world')
    data = s.recv(1024)
print('Received',repr(data))