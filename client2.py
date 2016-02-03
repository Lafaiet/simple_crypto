#!/usr/bin/python           

import socket               # Import socket module


def getJumped(c, jump):
	temp = (ord(c)-jump)%ord('z')
	result  = temp if temp>=ord('a') else ord('z')-(ord('a')-temp-1)

	return chr(result)


def poliDecode(message, cesar1, cesar2 ):
	
	encoded_temp = ''
	
	for c in message:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			c = getJumped(c, cesar2)
		encoded_temp += c
	
	encoded = ''
	
	for c in encoded_temp:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			c = getJumped(c, cesar1)
		encoded += c
	
	return encoded 


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
message =  s.recv(1024)

print 'Poli Encoded: %s'%(message)
print 'Decoded: %s'%(poliDecode(message, 3,2))

s.close                     # Close the socket when done