import socket
from termcolor import colored
sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

Ip= input("Enter the host name: ")

def portscanner(port):
    if sock.connect_ex((Ip,port)):
        pass
        #print(colored("the port %d is closed" %(port),"red")
    else:
        print(colored("The port %d is open" %(port)), "blue")
for port in range(1,1000):
    portscanner(port)
