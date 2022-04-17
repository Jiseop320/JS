import socket

server_IP = '203.250.133.88'
server_port = 10101
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#my_address = ('localhost', 20123)
#sock.bind(my_address)

server_addr = (server_IP, server_port)
message = input("Enter number: ")
#message = bytes(message, encoding = "utf-8")
#message = message.encode('utf-8)
#message = message.encode()

try:
    byte_sent = sock.sendto(message.encode(), server_addr)
    data, address = sock.recvfrom(BUFF_SIZE)
    print("Number of Type : {}" .format(data.decode()))

except Exception as e :
    print("Exception : %s" %str(e))

sock.close()