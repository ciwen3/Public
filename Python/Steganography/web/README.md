# Python Socket Notes
## Python Socket Library
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

For socket programming in Python, we use the official built-in Python socket library consisting of functions, constants, and classes that are used to create, manage and work with sockets. Some commonly used functions of this library include:
```python
    socket(): Creates a new socket.
    bind(): Associates the socket to a specific address and port.
    listen(): Starts listening for incoming connections on the socket.
    accept(): Accepts a connection from a client and returns a new socket for communication.
    connect(): Establishes a connection to a remote server.
    send(): Sends data through the socket.
    recv(): Receives data from the socket.
    close(): Closes the socket connection.
```




https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
### Server.py
```python
import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
#        if not data:
#            # if data is not received break
#            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
```







### Client.py
```python
import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
```
