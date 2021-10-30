# Overview

This is a simple peer to peer software that lets two different devices chat through a server. Before anything run the server. This is all that needs to be done with the server. It will display when a new device is connected and display the data transferred between clients. Once the server is running, the client.py file can be run from any device.

I wrote this to be able to connect my phone to my laptop. I havent ever learned much about networking, so I thought it would be fun to do a project to help me understand it better. Ideally, I would have liked to be able to send pictures as well. That is a goal I have to work on later down the road.

[Software Demo Video](https://youtu.be/XVRyNUKqdfw)

# Network Communication

This program is a peer-to-peer model, The server file is used for the clients to find each other. Any device that can run the client file can communicate with another who runs the same file. All data transmissions are done through TCP, and I selected a random port number of 12000 to use on each device. All data is encoded as utf-8 and sent as bits, where tey are then decoded for each client.

# Development Environment

This program was written in Visual Studio Code using two different Python files. Imported libraries include socket and threading.

# Useful Websites

- [Youtube video](https://youtu.be/u4kr7EFxAKk)
- [Python Documentation](https://docs.python.org/3/howto/sockets.html)

# Future Work

- I would like to build an app or GUI that makes the program more user friendly.
- The reason why I started this project was to be able to pass pictures from my phone to my laptop. I would still like to do this in the future, and at some point I will build this functionality.
- I hope to use this in the future to achieve my origional goal of building an app that included the ability for people to communicate with one another. (Obviously in a more sophisticated manner.)
