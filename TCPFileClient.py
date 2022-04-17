#!/usr/bin/python3
from socket import *
import os
import sys

host = ''
port = 10101

server_address = (host,port)
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(server_address)

print('Connect Complete')
filename = input('File name: ')
clientSock.sendall(filename.encode('utf-8'))

data = clientSock.recv(1024)
data_transferred = 0

if not data:
    print('Not Exist File %s' %filename)
    sys.exit()

nowdir = os.getcwd()
with open(nowdir+"\\"+filename, 'wb') as f:
    try:
        while data:
            f.write(data)
            data_transferred += len(data)
            data = clientSock.recv(1024)
    except Exception as ex:
        print(ex)
print('FileSending Complete : %s, File Data : %d' %(filename, data_transferred))