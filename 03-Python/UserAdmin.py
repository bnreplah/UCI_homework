# Administrator accounts list
adminList = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]

# Build your login functions below
def getCred():
    userInfo = {}
    userInfo["username"] = input("Username: ")
    userInfo["password"] = input("Password: ")
    return userInfo
def checkLogin( userInfo, adminList):
    loggedIn = False
    for admin in adminList:
        if admin["username"] == userInfo["username"]:
            if admin["password"] == userInfo["password"]:
                loggedIn = True
    return loggedIn

while False == checkLogin(getCred(), adminList):
    print("-----------------------------")
print("YOU HAVE LOGGED IN")