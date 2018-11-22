# Name: Snehith Raj Bada

import socket
import threading
import sys

BUFFER_SIZE = 1024                                              # Buffer size for the incoming message
TCP_IP = "localhost"                                            # IP address of the Server
TCP_PORT = int(input("Enter Port Number: "))                    # Port Number of the server on which it listens and accepts connections


class Thread(threading.Thread):                                 # Thread class to set up the connection with the client
    def __init__(self, ip, port, sock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("Client IP address : " + ip + " Port Number:" + str(
            port))                                              # Print the IP address and Port Number of the client

    def run(self):                                              # Method to process the incoming request from the Client
        try:
            request = self.sock.recv(BUFFER_SIZE)               # Receive request from the connected client and store
            print(request)
            filename = request.split()[1]                       # Rerieving the filename from the request
            print("Requested file is:", filename[1:])
            file = open(filename[1:])                           # Open the requested file
            data = file.read()                                  # Read the contents of the file and storing it
            file.close()                                        # Close the file
            print("Content of the file:", data)
            self.sock.send(b'HTTP/1.1 200 OK')                  # Sending status code 200 to the Client as the file was found
            self.sock.send(data.encode())                        # Sending the content of the file to the requested client
            print('File sent successfully')
            self.sock.close()                                   # Close the Client socket
        except IOError:
            self.sock.send(b'HTTP/1.1 404 Not Found')           # Send file not found error
            print("Requested file not found")
            self.sock.close()                                   # Close the Client socket


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Creating a Server socket object
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
threads = [];                                                   # To handle multiple Client connections

try:
    tcpsock.bind((TCP_IP, TCP_PORT))                            # Bind Server socket to the IP address and the port number
    print('Server bind is Complete')

except socket.error as msg:
    print(msg)  												# Display error message if server binding failed
    sys.exit()

tcpsock.listen(10)                                               # Initializing the Server socket to accept incoming Client connections
print('Server is ready to accept connections')

while True:
    connection, address = tcpsock.accept()                      # Establish the connection
    print("\nClient is connected with Ip Address:"
          + address[0] + ' and port number:' + str(address[1]))
    print(connection)
    print("Host name: " + str(connection.getpeername()))
    print('Socket Family: ' + str(connection.family))
    print('Socket Type: ' + str(connection.type))
    print('Time out: ' + str(connection.timeout))
    print('Socket Protocol: ' + str(connection.proto))
    conn = Thread(address[0], address[1], connection)
    conn.start()
    threads.append(conn)                                        # Append new connection
