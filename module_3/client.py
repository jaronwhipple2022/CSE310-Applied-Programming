"""
This file can be run on multiple machines an used to connect different devices and transfer data.
*** note the server.py file must be running ***
"""

# import libraries
import socket
import threading

# create variable to access socket library. use ip version 4, and tcp
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind varibale to ip address and port.
c.connect(('192.168.247.1', 12000))


# define and send name of device
name = str(input("\nEnter your name: "))
c.send(bytes(name, 'utf-8'))

def send():
    """ This function will be constantly running in the background to take input and send it as a message
    at any time. """

    # loop runs while program is still running to take input.
    while True:
        global name
        c.send(bytes((name + ": " + input("")), "utf-8"))

# access threading library to help multiple tasks run at once
message_thread = threading.Thread(target=send)
# let user close program with open threads
message_thread.daemon = True
# start the thread
message_thread.start()

# This will be constantly running in the background to take recieve messages at any time.
while True:
    data = c.recv(1024).decode()

    # connection is closed if no data is being recieved.
    if not data:
        break
    print(data)



