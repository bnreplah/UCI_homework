import os 
import shutil 
#imports shutil and os to be used in the document

#Defining the Stu_activities function
def stu_activities():
    #assigns the current working directory to destination before the directory is changed.
    #
    destination = os.getcwd()
    #changes the directory to Downloads in which it will search for all files starting with 'Stu_'
    #
    #assigns downloads to the path of downloads which is then used  in chdir
    #
    downloads = os.path.expanduser("~/Downloads")
    #changes the current working directory into the downloads folder
    #
    os.chdir(downloads)
    #assigns source to be a list of all the files in 'Downloads'
    #
    source = os.listdir(downloads)
    #scrolls through all the files in 'Downloads' to see if any 'startswith' "Stu_"
    #
    for files in source:
        #print(files)
        #checks to see if the iterated 'files' is a file and not a directory
        if (files.startswith("Stu_") or "Stu_" in files) and os.path.isfile(files):
            #uses 'shutil.copy' to copy the located file to the 'destination' which was defined earlier
            #
            shutil.copy(files,destination)#if wanted to copy dir too woul used 'copytree'
            #the print command below is used for debugging to see in the listed files where the match was found
            #print("-------------------")
stu_activities()
