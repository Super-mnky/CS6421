#!/usr/bin/env python3
import hashlib
import socket

HOST = ''  # Standard loopback interface address (localhost)
PORT = 5555        # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(0)

print ("Now listening for connections...")

KVstore = {}

while True:
    conn, addr = s.accept()
    print ('Connected by', addr)

    data = conn.recv(1024)
    clientInfo = str.split(data)

    #need a try catch block, wont always be 3 array objects
    operation = clientInfo[0]
    keyHash = (hashlib.sha1(clientInfo[2])).digest()
    value = clientInfo[1]
    
    print (keyHash)
    break

    print(clientInfo[0] + " " + clientInfo[1] + " " + clientInfo[2])
    if (operation.lower() == 'stats'):
        print ("this is where we give him the damn stats")
        response1 = len(KVstore)
        conn.send(response1)

    if (operation.lower() == 'set'):
        print ("This is where I implement 'set' method")
        KVstore[keyHash] = value

    if (operation.lower() == 'get'):
        print ("Here I implement get method")
        response2 = KVstore.get(keyHash)

        print response2
        #conn.send(response2)

    conn.close()
    print
    #print

