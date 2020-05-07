import random
import getpass
import hashlib
import f
import CreateUsr


def auth():
    
    #convert Users to a list
    User_file = open('Users', 'r')
    User_lines = User_file.readlines()
    User_file.close()
    
    #convert PassHash to a list
    PassHash_file = open('PassHash', 'r')
    PassHash_lines = PassHash_file.readlines()
    PassHash_file.close()


    while True:
        try:
            
            User = input("Username:  ")#Input username
            ListNum = User_lines.index(User)
            

            PassHash = hashlib.sha512(getpass.getpass().encode('utf-8')).hexdigest()

            
            if PassHash == PassHash_lines[ListNum].rstrip():
                f=open(TmpUsrStr, w)
                f.write(User)
                f.close()
                break
            else:
                print()
                print("Incorrect Password")
                print()
            
            
            
        except(ValueError):
            print()
            print("Incorrect Username")
            print()






auth()
print("Authentication Successful")
