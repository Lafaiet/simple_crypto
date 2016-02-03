#!/usr/bin/python           

import socket               # Import socket module

def monoEncode(message, cypher ):
	
	encoded = ''
	
	for c in message:
		if c in cypher:
			c = cypher[c]
		encoded += c
	
	return encoded 


cypher = {'a': 'm', 'c': 'b', 'b': 'n', 'e': 'c', 'd': 'v', 'g': 'z', 'f': 'x', 'i': 's',
 'h': 'a', 'k': 'f', 'j': 'd', 'm': 'h', 'l': 'g', 'o': 'k', 'n': 'j', 'q': 'p',
  'p': 'l', 's': 'i', 'r': 'o', 'u': 'y', 't': 'u', 'w': 'r', 'v': 't', 'y': 'w',
   'x': 'e', 'z': 'q'
 }


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print 'Waiting for client connection...'

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
message = 'Hello fibre!'
c.send(monoEncode(message, cypher))
c.close()                # Close the connection
