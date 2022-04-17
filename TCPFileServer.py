#!/usr/bin/python3
from socket import *
from os.path import exists
import sys

host = ''
port = 10101

server_address = (host,port)
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(server_address)
serverSock.listen(1)

connectionSock, addr = serverSock.accept()

print(str(addr),'to Send')

filename = connectionSock.recv(1024)
print('Sending Data : ', filename.decode('utf-8'))
data_transferred = 0

if not exists(filename):
    print("no file")
    sys.exit()

print("File %s Sending..." %filename)
with open(filename, 'rb') as f:
    try:
        data = f.read(1024)
        while data:
            data_transferred += connectionSock.send(data)
            data = f.read(1024)
    except Exception as ex:
        print(ex)
print("FileSending %s, Data %d" %(filename, data_transferred))