'''
i)Program to find IP address from Domain Name.
ii)Program to find Server Name from IP address
'''
import socket
import sys

print ('Welcome to DNS to IP Address')
URL=sys.argv[1]

addr1 = socket.gethostbyname(URL)

print(addr1)
print ('WelCome IP address to DNS')
IP= sys.argv[2]
addr6=socket.gethostbyaddr(IP)
print (addr6)

if len(URL) <= 0:
    print("[+]insert the url[+]")
    sys.exit()

if len(IP) <= 0:
    print("[+]insert the IP[*]")
    sys.exit()