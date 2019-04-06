import os
#imports os 

#defines the function main to create the folder directory system
def main():
    #
    #checks to see if the 'CyberSecurity-Notes' directory already exits
    #
    if os.path.isdir("CyberSecurity-Notes") == False:
        #uses 'os.mkdir' to make a directory 'CyberSecurity-Notes'
        #
        os.mkdir("CyberSecurity-Notes")
        #changes the path to the new directory
        #
        cur_path = os.path.join("CyberSecurity-Notes")
        #runs a for loop to create 24 iterations of i
        #
        for i in range(1,25):
            #makes a directory under the 'cur_path' with the name 'Week' + the value of 'i' 
            #
            os.mkdir(cur_path + "/" + "Week " + str(i))
            #joins the path into the folder that was just created
            #  
            file_path = os.path.join(cur_path+ "/"+ "Week " + str(i))
            #iterates through a range of 1-4 producing 3 lesson folders in the current 'Week' folder
            #
            for b in range(1, 4):
                #makes the new directory with each 'Day'
                #
               os.mkdir(file_path + "/" + "Day " + str(b))
               b +=1  #changes the iterated value
            i +=1 #changes the iterated value
    #if the directory exits prints out error message and aborts:        
    else:
        print("----------FILE SYSTEM ALREADY EXISTS, CREATION OF FILE SYSTEM ABORTED!!-----------")
#main()