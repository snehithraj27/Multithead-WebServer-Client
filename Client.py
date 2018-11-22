# Name : Snehith Raj Bada

import socket
import time

TCP_IP = input("Enter Host IP Address : ")                     # Enter the IP Address of the Server
TCP_PORT = int(input("Enter Port Number : "))                  # Enter the port number of the Server
BUFFER_SIZE = 1024

tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Creating a Client socket object
tcpsoc.connect((TCP_IP, TCP_PORT))                             # Establishing a connection with the Server using the
                                                               # Ip Address and port number
print("Connected to the Server")

file = input("Enter Filename : ")                              # Enter the file to be requested from the Server
print("\nHostname : ", socket.gethostname())
print("Port Number : ", TCP_PORT)
print("The Host IP Address : ", TCP_IP)
print("The filename : ", file)
print("Peer name : "+str(tcpsoc.getpeername()))

tcpsoc.send(b'msg /'+file.encode())                            # Requesting file from the Server
Start = time.time()                                            # Store the time at which the request was made
while True:                                                    # While loop handles the incoming file from the Server
    content = tcpsoc.recv(BUFFER_SIZE)                         # Read the contents of the file
    if not content:                                            # If no content is present in the file
        break                                                  # Break the loop
    print(content)
End = time.time()                                              # Store the time at which the file was received
rtt = End - Start                                              # Calculate the Round Trip Time (RTT)

print("\nRound Trip Time (RTT) : "+str(rtt) + " Seconds ")
print('Socket Family : '+str(tcpsoc.family))
print('Socket Protocol : '+str(tcpsoc.proto))
print('Socket Type : '+str(tcpsoc.type))
print('Time out : '+str(tcpsoc.timeout))
tcpsoc.close()                                                  # Close the Client Socket
print('\nThe Connection is closed')
