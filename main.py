import random
import getpass
import hashlib
import f
import CreateUsr

print('what are you looking at fijdhsifguygsdyufagsd')

def auth():
    while True:
        Username = input("Username:  ")
        Password = hashlib.sha512(getpass.getpass().encode('utf-8')).hexdigest()
        print(Password)


auth()