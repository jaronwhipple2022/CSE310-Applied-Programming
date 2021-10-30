"""
This file is the server that will connect the clients and allow information to pass between them.
"""

# import libraries
import socket
import threading

# create variable to access socket library. Use ip version 4 and tcp.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind varibale to ip address and port.
server.bind(('192.168.247.1',12000))

# set server to listen for connections or clients.
server.listen(1)
print("\nWaiting for connections ... \n")

# set empty list to hold all the connected devices.
devices = []

# define the handler function to manage incoming data
def running_chat(client, address):
    global devices

    # run loop in background
    while True:

        # define data
        data = client.recv(1024).decode()
        data = "\n          " + data

        # display data on server terminal
        print(data)

        # temporarily remove device that sent the message
        devices.remove(client)

        # send the data to all connected devices
        for device in devices:
            device.send(bytes((data), "utf-8"))

        # add the device that sent the message
        devices.append(client)

        # when data is not being recieved from a given device, it will terminate and close the connection.
        if not data:
            devices.remove(client)
            client.close()
            break

# While server is running and someone connects:
while True:

    # accept client, store their ip adress, add client to list of connected people
    client, address = server.accept()
    name = client.recv(1024).decode()
    devices.append(client)
    print(client)

    # access threading library to help multiple tasks run at once
    connection_thread = threading.Thread(target=running_chat, args=(client,address))
    # let user close program with open threads
    connection_thread.daemon = True
    # start the thread
    connection_thread.start()
    
    print("\n", name, " has connected.\n")

    # tell other devices who has connected.
    for device in devices:
        device.send(bytes(("\n" + name + " has connected.\n"), "utf-8"))

