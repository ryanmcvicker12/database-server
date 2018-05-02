
#database script to add data sent from the client to a server

import sqlite3

from dataserver import Server

#inherited method would allow information to be sent to the client
class database:

    def __init__(self):
        self.conn = sqlite3.connect('serverdata.db')
        self.c1 = self.conn.cursor()

        self.c1.execute("CREATE TABLE IF NOT EXISTS data(user_data TEXT)")
        self.serv = Server()


    def add_to(self,data):

        try:
            self.c1.execute("INSERT INTO data VALUES(?)",(data,))#Wil insert the values into the database
            self.conn.commit() #saves all changes made to the database
        except Exception as e:#going to send message to the client if action
        #couldent be completed
            message = "data couldent be added"#message the server will send back to client
            self.serv.sendData(message) #uses method from the server class


    def get_all(self):#send all data to the client maybe in file form?

        self.c1.execute("SELECT * FROM data")#grabs all data from the database
        for new in self.c.fetchall(): #grabs all data from the table
            Server.sendData(str(new))#will send the data back to the client





if __name__ == '__main__':
    database()
