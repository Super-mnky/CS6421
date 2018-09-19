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

    operation = clientInfo[0]
    #key = (hashlib.md5(clientInfo[2])).digest()

    if (operation.lower() == 'stats'):
        entries = ((str(len(KVstore))))
        conn.send("\nThe number of entries is: " + entries)

    if (operation.lower() == 'set'):
        key = clientInfo[1]
        value = clientInfo[2]
        KVstore[key] = value
        conn.send("\nSET command succesfully executed.")

    if (operation.lower() == 'multiset'):
        index = 1
        while index < len(clientInfo):
            KVstore[clientInfo[index]] = clientInfo[index+1]
            index = index + 2
        conn.send("\nMultiset command succesfully executed.")

    if (operation.lower() == 'get'):
        key = clientInfo[1]
        keyResponse = KVstore.get(key)
        conn.send("\nThe value for '" + key + "' is: " + keyResponse)
        
    if (operation.lower() == 'multiget'):
        index = 1
        while index < len(clientInfo):
            keyResponse = KVstore.get(clientInfo[index])
            conn.send("\nThe value for '" + clientInfo[index]  + "' is: " + keyResponse)
            index = index + 1
        conn.send("\n\nMultiget command succesfully executed.")


    conn.close()
    print
    #print

