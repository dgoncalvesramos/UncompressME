import socket
import base64
import sys 
import re
import zlib

def extract_encoded_string_and_decompress_it(text):
	pattern = re.compile(r"my string is '([^']+)'")
	match = pattern.search(text)
	if match:
		encoded_string = match.group(1)
		decoded_bytes = base64.b64decode(encoded_string)
		uncompress_string = zlib.decompress(decoded_bytes)
		decoded_string = uncompress_string.decode('utf-8') 
	else:
		sys.exit("Encoded string was not found")
	return decoded_string
	
# Paramètres
HOST = 'challenge01.root-me.org'  # Hostname
PORT = 52022        			  # Port du serveur

# Créer le socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Reception de la réponse
response = s.recv(1000).decode()
print(response)

i=4
while i>0:

	#Envoie du message
	message = extract_encoded_string_and_decompress_it(response) + '\n'
	s.send(message.encode())

	#Réception du flag
	response = s.recv(1000).decode()
	print(response)
	i-=1
	
#fermeture de la socket
s.close()



