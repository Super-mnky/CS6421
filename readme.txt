# Welcome to Jerry Jones IV's simple Key-Value store system! 

#### THE SERVER
Starting the server is very simple. It is configured to run on localhost, but in later configurations it will be customizedable via the command line. To start it simply run the command, 
# python PythonServer.py. 
If it initializes correctly, the feedback should indicate it:
#Now listening for connections...
If you see this, you are good to go!

THE CLIENT
The client is used via a similiar command, followed by the IP that you are looking to connect to. Because Server is default set to localhost, you will want to as well. Client by default connects to the correct port. Lastly, is the command you wish to issue.
An exmaple: # python PythonClient.py localhost <command>
These commands are defined in the protocols. The entire command using protocols is placed within quotes. All commands are case-insensitive.

THE PROTOCOLS - STATS
You may issue the STATS command, to return the total number of items currently held in the store.
# python PythonClient.py localhost "stats"

THE PROTOCOLS - SET
You may set a Key-value pair to be held in the KV system. You may do so in the following way.
# python PythonClient.py localhost "set money 1000". 
or more generally, 
# python PythonClient.py localhost "set KEY VALUE"
If the key is already in the store, the server will update the value. The server will confirm successful or failed execution. 

THE PROTOCOLS - MULTISET
In a similiar manner, you may issue a multiset command for multiple key-value pairs. An example:
# python PythonClient.py localhost "multiset money 1000 debt 0 password 12345admin"
or more generally
# python PythonClient.py localhost "multiset KEY VALUE KEY VALUE KEY VALUE...."
The server will confirm success or failed execution. 

THE PROTOCOLS - GET
You may retrieve values that are in the KV system with GET.
# python PythonClient.py localhost "get money"
or more generally,
# python PythonClient.py localhost "get KEY"
The server will return the value that is associtated with that key.

THE PROTOCOLS - MULTIGET
In a similiar manner, you may retrieve multiple values from keys as well:
# python PythonClient.py localhost "multiget money debt password"
or more generally
# python PythonClient.py localhost "multiset KEY KEY KEY KEY KEY...."
The server will confirm success or failed execution. 

PERFORMANCE TESTING
Using the performance testing script is easy. To test the system performance in latency, navigate to the performancetesting directory and you will find the performance testing program, 'perfTest', along with 4 other programs. The testing program is easy to use, assuming all the protocols above all succesfully executed. There are test cases for all the protocols. It willl return the minumum, maximum, and average latency for your trial. This is the format you will use.
# ./perfTest ptSET.py 25
or more generally
# ./perfTest <FileToTest> <NumberOfTrials>
The files were intended to run SET before GET, and MULTISET before MULTIGET.

ADDITIONALLY
The wiki homepage has screen shots of the performance results in case you you can't be bothered to do them yourself. 
https://github.com/Super-mnky/CS6421/wiki
