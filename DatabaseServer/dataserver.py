#server to add data into database
#save data to file
import socket
import sqlite3
from Database import * #label inherited methods
#thread to run server?
#inherits the server class in order to use the sendData method to send
#information back to the client
class Server:

    def __init__(self):
        self.server = socket.socket()
        self.host = '127.0.0.1'
        self.port = 5000
        self.server.bind((self.host,self.port))
        self.server.listen(1)
        self.c, self.addr = self.server.accept()
        self.datab = database()


        while True: #loop to constantly accept data and add it to the database

            #take data sent from the client
            data2 = self.c.recv(1024).decode('utf-8')#data from the client
            if data2 == 'show all':
                self.datab.get_all() #method from database

            else:
                self.datab.add_to(data2) #inherited from th database class

    def sendData(self,data):
        self.message = data.encode('utf-8')
        self.c.send(self.message) #sends data back to the client

if __name__ == '__main__': #runs the server program
    Server().__init__
