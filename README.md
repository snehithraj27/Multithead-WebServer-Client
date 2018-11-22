# Multithead-WebServer-Client
Multithreaded Web Server which interacts with any standard Web Clients.

Description: 
- The Web Server and Web Client communicate using a text-based protocol called HTTP.
- The server being multi-threaded will be able to handle multiple requests concurrently. 
- The main thread (server), listens to a specified port like the standard port for HTTP (8080).
- Upon receiving a HTTP request, the server sets up a TCP connection to the requesting client and serves the request 
  in a separate thread using a new port. After sending the response back to the client, it closes the connection.
  
- The client requests for a file from the server. 
  1.	If this file exists, the server responds with ‘HTTP/1.1 200 OK’ 
  2.	If the file doesn’t exists, the server responds with ‘HTTP/1.1 404 Not Found’.
- The following information are extracted from the connection objects: 
  1.	RTT for the client request
  2.	Relevant details like Host Name of the server, socket family, socket type, protocol, timeout and get peer 
      name are extracted on client side and server side.
      
 Steps to Execute :
 1.	Run server.py.
    Enter the Port Number (E.g.: 8080). Server gets bound to the port and waits for incoming connections from the client.
 2.	Run Client.py 
    Enter IP Address and the port number of the Server. The Client is connected to the Server.
    Multiple Clients can be connected to the Server.
 3.	Enter the file name to be requested from the server.
 4.	The server receives the request process it
 5.	i) If the Server finds the file it responds with ‘HTTP/1.1 200 OK’ and sends the file content
    ii) If the Server doesn’t find the file it responds with ‘HTTP/1.1 404 Not Found’.
 6.	The Client receives the response from the Server and displays it.
 7.	Relevant details like Host Name of the server, socket family, socket type, protocol, timeout and get peer name are displayed on client side and server side.


