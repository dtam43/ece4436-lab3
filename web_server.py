# Import socket module
from socket import *
import sys # In order to terminate the program
server_socket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
port = 6789
server_socket.bind(('', port))
server_socket.listen(1)
print('Web server established on port: ', port)

host = gethostname()
ip = gethostbyname(host)
print('Host IP address: ', ip)
# Fill in end

# Establish the connection
print('Ready to serve...')
conn_socket, addr = server_socket.accept()

try:
    msg = conn_socket.recv(1024)
    filename = msg.split()[1]
    f = open(filename[1:])
    data = f.read() 

    # Send one HTTP header line into socket
    # Fill in start
    conn_socket.send('\nHTTP/1.1 200 OK\n\n'.encode())
    # Fill in end

    # Send the content of the requested file to the client
    for i in range(0, len(data)):
        conn_socket.send(data[i].encode())
    
    conn_socket.send("\r\n".encode())
    conn_socket.close()

except IOError:
    #Send response message for file not found
    #Fill in start
    conn_socket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
    #Fill in end

    #Close client socket
    #Fill in start
    conn_socket.close()
    #Fill in end

server_socket.close()
    
#Terminate the program after sending the corresponding data
sys.exit()