from dbhelper import DBHelper

def main():
    db=DBHelper()
    
    while True:
        print("***********WELCOME***********")
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        
        try:
            choice=int(input())
            if(choice==1):
                #insert
                uid=int(input("Enter userid: "))
                uname=input("Enter username: ")
                uphone=input("Enter users phonr")
                
                db.insert_user(uid,uname,uphone)
                pass
            elif(choice==2):
                #display user
                db.fetch_all()
                pass
            elif(choice==3):
                #delete
                uid=int(input("enter userid to delete: "))
                db.delete_user(uid)
                pass
            elif(choice==4):
                #update
                uid=int(input("Enter userid where to update: "))
                uname=input("Enter new username: ")
                uphone=input("Enter new users phonr")
                pass
            elif choice==5:
                break
            else:
                print("Invalid input! try again..")
        except Exception as e:
            print(e)
            print("Invalid Details! try again....")
            
if __name__=="__main__":
    main()
