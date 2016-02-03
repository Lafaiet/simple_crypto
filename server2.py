#!/usr/bin/python           

import socket               # Import socket module

def getJumped(c, jump):
	temp = (ord(c)+jump)%ord('z')
	result  = temp if temp>=ord('a') else ord('a')-1+temp

	return chr(result)


def poliEncode(message, cesar1, cesar2 ):
	
	encoded_temp = ''
	
	for c in message:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			c = getJumped(c, cesar1)
		encoded_temp += c
	
	encoded = ''
	
	for c in encoded_temp:
		if ord(c) >= ord('a') and ord(c) <= ord('z'):
			c = getJumped(c, cesar2)
		encoded += c
	
	return encoded 


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print 'Waiting for client connection...'

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
message = 'Ola como vai?'
c.send(poliEncode(message, 2,3))
c.close()                # Close the connection
