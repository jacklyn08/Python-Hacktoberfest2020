import socket
import sys

#here i create an argument

port = sys.argv[1]
if int(port) >= 0:
    print("[*]insert the port[*]")
    sys.exit()
#here i create the server socket and I bind it for any incoming connection

s = socket.socket()
try:
    s.bind(('',int(port)))
except socket.error as error:
    print(error)

s.listen()
sock,ip = s.accept()
print("[+]" + ip + "connected" + "[+]")
