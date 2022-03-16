#!/usr/bin/python3

import socket

IP = "10.9.0.6" # dst ip
PORT = 9090 # dst port

#data = b'Hello, World!'

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.sendto(data, (IP,PORT))



while True:
	data = input()
	data_in_bytes = bytes(data, 'utf-8')
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(data_in_bytes, (IP,PORT))
	
