import mysql.connector 

class DBHelper:
    def __init__(self):
        self.con= mysql.connector.connect(host='localhost',
                                   port='3306',
					     user='root',
                                   password='root',
                                   database='pythontest')
        
        #creating table
        query='create table if not exists user(userID int primary key,userName varchar(200), phone varchar(12))'
        cur= self.con.cursor()
        cur.execute(query)
        print("Created")
        
    #Insert in table
    
    def insert_user(self,userid,username,phone):
        query="insert into user (userID, userName, phone) values({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()   #make permanant changes in database
        print("user saved to database")
        
    #Fetch all(read)
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User id: ",row[0])
            print("User name: ",row[1])
            print("Phone: ",row[2])
            print()
            
    #Update
    def update_user(self,userid, newname,newphone):
        query="update user set userName='{}', phone='{}' where userID={}".format(newname,newphone,userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Updated")
        
        
        
    #Delete user
    def delete_user(self,userID):
        query="delete from user where userID={}".format(userID)
        print(query)

        cor=self.con.cursor()
        cor.execute(query)
        self.con.commit()
        print("Deleted")




