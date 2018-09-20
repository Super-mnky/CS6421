# A simple client to interact with the KVstore server.
# Written by Jerry Jones IV

#!/usr/bin/python2.7
import socket
import argparse
import sys
import select

# to enable input commands, we add sys.argvs to catch and assignthem to vars
#host=sys.argv[1] if len(sys.argv) > 1 else "somevalue"
#userData=sys.argv[2] if len(sys.argv) > 1 else "somevalue3"


#as specified by server, we connect on port 5555
host = 'localhost'
portnum = '5555';

#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

#connect and send the message
s.connect ((host,5555))

userData = "get money"
s.send(userData)

#we always send message first, but where appropriate we recieve data also
while True:
    
    #find what sockets are avaiable 
    socket_list = [sys.stdin, s]
    ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])

    #for all sockets,  read and print the data from the server
    for sock in ready_to_read:
            if sock == s:
                data = sock.recv(4096)
                #print data
                #if blank, kill the client
                if not data :
                    #print 'Disconnected from chat server'
                    sys.exit()

