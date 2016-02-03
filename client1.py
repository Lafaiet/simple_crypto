#!/usr/bin/python           

import socket               # Import socket module


def monoDecode(message, cypher):
	inv_map = {v: k for k, v in cypher.items()}
	
	decoded = ''
	
	for c in message:
		if c in cypher:
			c = inv_map[c]
		decoded += c
	
	return decoded 


cypher = {'a': 'm', 'c': 'b', 'b': 'n', 'e': 'c', 'd': 'v', 'g': 'z', 'f': 'x', 'i': 's',
 'h': 'a', 'k': 'f', 'j': 'd', 'm': 'h', 'l': 'g', 'o': 'k', 'n': 'j', 'q': 'p',
  'p': 'l', 's': 'i', 'r': 'o', 'u': 'y', 't': 'u', 'w': 'r', 'v': 't', 'y': 'w',
   'x': 'e', 'z': 'q'
 }


s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
message =  s.recv(1024)

print 'Mono Encoded: %s'%(message)
print 'Decoded: %s'%(monoDecode(message, cypher))

s.close                     # Close the socket when done