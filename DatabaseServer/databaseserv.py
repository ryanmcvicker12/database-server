#this is another attempt at creating the server for databases

"""

OVERVIEW:
    This project should be a server any client can connect to across the internet
    and add data to the database 

    """


import sqlite3
import socket
import time #to keep track of the performance of the software



class Server(database):#class to start up the server and allow data to be sent back to the client


    def __init__(self):
        self.start = time.time()#start tracking how long it takes for the server to be made
        self.server = socket.socket() #create socket object in TCP (Transmission, Control, Protocol)
        self.port = 5000
        self.host = '127.0.0.1'

        self.bind((self.host,self.port)) #binds the port and host, officially creating the server
        self.stop = time.time()
        print("server took : {} time to start".format(self.start - self.stop))


        self.server.listen(1) #server will only accept and listen to one connection
        self.client, self.addr = self.server.accept() #accepts the connection from the client
        while True:#going to listen for data from the client and pass any string into the inheried method from the database class




    def send_data(self,data): #going to accept data, thus calling the inherited method from the database class

        #first we need to break the string into a tuple of separate strings
        self.data = self.server.recv(1024).decode('utf-8')
        self.string = tuple(self.data.split(' ')) #creates tuple for the data to be entered
        #first element of the list should be the table name
        self.tname = self.string[0] #gets the table name
        #now we split the tuple as the only elements we need are [1:3]
        self.split_data = self.string[1:3]
        #now we call the method from the database class

        if addTo(self.split_data, self.tname):
            addTo(s)





class database:


    def __init__(self): #define the databases attributes here such as table name etc.
            self.conn = sqlite3.connect("library.db")
            self.c = self.conn.cursor()
            self.c.execute('CREATE TABLE IF NOT EXISTS books(name TEXT, author TEXT, genre TEXT)') #creates the table of books
            self.c.execute('CREATE TABLE IF NOT EXISTS employees(name TEXT, age INT, salary REAL)') #creates table of employees

    def addTo(self,data,table_name): #should recieve data in the form of a tuple
        #the server class should recieve a boolean of true or false depending whether the data is sent
        try:
            self.c.execute("INSERT INTO %s VALUES(?,?,?)" % (table_name), data)
            return True
        except Exception as e:
            return False
