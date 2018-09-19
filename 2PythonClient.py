
# CS 6421 - Simple Message Board Client in Python
# T. Wood
# Run with:     python msgclient.py

import socket
import argparse
import sys
import select

host=sys.argv[1] if len(sys.argv) > 1 else "somevalue"
#userName=sys.argv[2] if len(sys.argv) > 1 else "somevalue2"
userData=sys.argv[2] if len(sys.argv) > 1 else "somevalue3"


# host = "localhost";
portnum = 5555;

#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port

s.connect ((host,5555))
s.send(userData)

while True:
    
    socket_list = [sys.stdin, s]
    ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])

    for sock in ready_to_read:
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                print data
                if not data :
                    print 'Disconnected from chat server'
                    sys.exit()

