import os
import hashlib
import csv
#imports os, hashlib, csv to be used
#
#csv_path creates a path to the csv unhashaed file
#######################################################
######PADDING:::: OPENING CSV FILE :::::PADDING########
#######################################################
#
csv_path = os.path.join("UserInfo.csv")
#
#opens the file to be read
#
csv_file = open(csv_path)
#
#reads csvfile into contents
#
contents = csv.reader(csv_file)

csv_hash = open("UserInfo_Hashed.csv", "w", newline= '')
writer = csv.writer(csv_hash)
##########################################################################################################
##########################################################################################################
def hasher(tobe):
    s256 = hashlib.sha256()
    s256.update(tobe.encode('utf-8'))
    return s256.hexdigest()

#
#Name 0
#email 1
#password 2
#phone 3
#Address 4
#city 5
#zip 6
#country 7
#credit card number 8
#CVV 9
#balance 10
#

for index, row in enumerate(contents):
    
    tempList = row
    if index != 0:   
        tempList[2] = hasher(tempList[2])
        tempList[8] = hasher(tempList[8])
        tempList[9] = hasher(tempList[9])
    print(tempList)
    writer.writerow(tempList)
csv_hash.close()
csv_file.close()