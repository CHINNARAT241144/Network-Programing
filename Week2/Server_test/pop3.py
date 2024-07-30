import poplib
from email.message import EmailMessage

server = "192.168.127.134"
user = "dewinet"
passwd = "Dew241144@"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msNum = len(server.list()[1])

for i in range(msNum):
    for msg in server.retr(i+1)[1]:
        print(msg.decode())