import socket

host = '0.0.0.0'
port = 10101
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)

while True:
    print("\nwaiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    print("echo message : {}".format(message.decode()))

    data = message.decode()
    try:
        num = int(data)
        if num % 2:
            answer = "Odd number"
        else:
            answer = "Even number"
    except valueError:
        answer = "Not number"
    sock.sendto(answer.encode(), client_address)

sock.close()

sock.close()