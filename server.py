import socket
import sys

FORMAT = 'utf-8'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
# updated format for print to stderr
print('starting up on %s port %s' % (server_address), file = sys.stderr)
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection', file = sys.stderr)
    connection, client_address = sock.accept()

try:
    print('connection from', client_address, file = sys.stderr)

    while True:
        data = connection.recv(16)
        print('received "%s"' % (data), file = sys.stderr)
        if data:
            print('sending data back to the client', file = sys.stderr)
            connection.sendall(data.encode(FORMAT))
        else:
            print('no more data from', client_address)
            break
finally:
    connection.close()
