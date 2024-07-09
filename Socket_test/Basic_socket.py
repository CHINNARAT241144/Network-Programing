import socket

try:
    print("Fully qualityfied domain name" + socket.getfqdn("B.B.B.B"))
    print("Host name to IP address: " + socket.gethostbyname("www.python.org"))
    print("Host name to IP address, extended: " + str(socket.gethostbyname_ex("www.python.org")))
    print("Get host name of local machie" + socket.gethostname)
except Exception as err :
    print("Error: "+ str(err))