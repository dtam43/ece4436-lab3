import socket
import time

# Set up socket with same port number
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 12000)
client_socket.settimeout(1) # Set timeout to 1s

# Send 10 pings
for i in range(1, 11):
    # Set start time and message
    start = time.time()
    msg = 'Ping #' + str(i) + ' ' + time.ctime(start)
    try:
        # Send ping
        sent = client_socket.sendto(msg.encode('utf-8'), server_addr)
        print('Sent ' + msg)

        # Retrieve response
        data, server = client_socket.recvfrom(4096)
        print('Received ' + str(data))

        # Calcualte RTT
        end = time.time()
        elapsed = end - start
        print('RTT: ' + str(elapsed) + ' seconds\n')
    
    # On timeout 
    except socket.timeout:
        print('#' + str(i) +  ' Request timed out\n')

# Close socket
client_socket.close()