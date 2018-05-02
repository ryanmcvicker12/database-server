#program to write all data inside of a database
#then print out all the data
import sqlite3



conn = sqlite3.connect("why.db")


c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(userdata TEXT,name INT)")

values = [
("ryan",12),
("dave",21),
("michael",45),
("joe",67),
]

c.executemany("INSERT INTO data VALUES(?,?)",values)
c.execute("SELECT * FROM data")

with open("newfile.txt","w+") as f:
    try:
        f.write(str(c.fetchall()))
    except Exception as e:
        print(e)


with open("newfile.txt","r") as t:
    print(t.read())
