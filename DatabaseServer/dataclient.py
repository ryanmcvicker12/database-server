#script to send data and have server add the data into an sqlite3 database
import socket
#try to use with statement for improved readability


#how to use threading??


#should client be OOP?
def Client():#client is going to send data to the server while server will add
#data to an sqlite3 database
    client = socket.socket()
    host = '127.0.0.1' #server port will be the loopback address
    port = 5000
    client.connect((host,port))
    data = input("please enter any data to be added to the sqlite3 database:")
    while data != 'q':
        client.send(data.encode('utf-8')) #sends data to the server
        data = input("please enter any data to be added to the sqlite3 database:")

    client.close() #closes the connection

Client()#runs the cliet program, no if__name__ == __main__
