import os
import hashlib
import  csv
info = []
csv_path = os.path.join("UserInfo_Hashed.csv")

csv_file = open(csv_path, 'r')

contents = csv.reader(csv_file)
def hasher(tobe):
    s256 = hashlib.sha256()
    s256.update(tobe.encode('utf-8'))
    return s256.hexdigest()


def validate(credentials):
    for row in contents:
        if credentials[0] == row[1]:
            print(hasher(credentials[1]))
            if hasher(credentials[1]) == row[2]:
                print("Welcome, " + str(row[0]) + ", Your Address is : " + str(row[4]) + "\n Your balance is :" + str(row[10]))
                return True
    return False
    

            



attempts = 0

while attempts < 3:
    
    
    print("-----------------LOCKED---------------------")
    print("----------                        ----------")
    print("----------                        ----------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    email = input("Email:")
    passwd = input("Password:")
    cred =[email, passwd]
    print(cred)
    if validate(cred) == True:
        attempts += 3
        print("----------------     unlocked      ---------")
        print("----------                        ----------")
        print("----------                        ----------")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("--------------------------------------------")
