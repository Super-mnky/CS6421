# This is a KV pair server.
# Writte by Jerry Jones IV

#!/usr/bin/env python3
import hashlib
import socket


#standard loopback interface and arbirarily chosen port 5555, initialize KVstore
HOST = ''          
PORT = 5555        
KVstore = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(0)

print ("Now listening for connections...")

while True:
    conn, addr = s.accept()
    print ('Connected by', addr)
    
    try:
        #recieve user submitted command then parse it on 'spaces' to work with the items individually
        data = conn.recv(1024)
        clientInfo = str.split(data)
        operation = clientInfo[0]

        if (operation.lower() == 'stats'):
            entries = ((str(len(KVstore))))
            conn.send("\nThe number of entries is: " + entries)

        elif (operation.lower() == 'set'):
            key = clientInfo[1]
            value = clientInfo[2]
            KVstore[key] = value
            conn.send("\nSET command succesfully executed.")

        #for multi KV pairs, once we've logged 1 pair, loop through info incrementing by 2 to always catch the KV pairs
        elif (operation.lower() == 'multiset'):
            index = 1
            while index < len(clientInfo):
                KVstore[clientInfo[index]] = clientInfo[index+1]
                index = index + 2
            conn.send("\nMultiset command succesfully executed.")

        elif (operation.lower() == 'get'):
            try:
                key = clientInfo[1]
                keyResponse = KVstore.get(key)
                conn.send("\nThe value for '" + key + "' is: " + keyResponse)
            except:
                conn.send("\nThis key is not in the KV store")
        
        #same as multiset
        elif (operation.lower() == 'multiget'):
            index = 1
            try:
                while index < len(clientInfo):
                    keyResponse = KVstore.get(clientInfo[index])
                    conn.send("\nThe value for '" + clientInfo[index]  + "' is: " + keyResponse)
                    index = index + 1
                conn.send("\n\nMultiget command succesfully executed.")
            except:
                conn.send("\nOne or more of the keys is not in the KV store.")

        else:
            conn.send("\nInvalid operation specified.")
    #here to catch invalid operations or incorrect formatting of KV pairs
    except:
        conn.send("\nImproper formatting. Terminating session.")

    conn.close()
    print
    #print

