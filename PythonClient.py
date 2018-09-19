
# CS 6421 - Simple Message Board Client in Python
# T. Wood
# Run with:     python msgclient.py

import socket
import argparse
import sys

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
s.connect((host, 5555))

# store the 1st raw data stream as the name
# userName = raw_input()
# and the 2nd raw data stream as the string to be delivered
# userData = raw_input()

#this is because the message server delinates name vs data by the \n char
#so we smash it all together using the delinater then send it
#totalData = userName + "\n" + userData + "\n"

totalData = userData
s.send(totalData)

#s.close
print("\nSent message to server!")
