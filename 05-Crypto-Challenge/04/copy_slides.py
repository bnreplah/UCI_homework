import os 
import shutil 
#imports os and shutil

def pptx_copy():
   
    #assigns the current working directory to destination before the directory is changed.
    #
    destination = os.getcwd()
    #changes the directory to Downloads in which it will search for all files ending with '.ppt' or '.pptx'
    #
    #assigns downloads to the path of downloads which is then used  in chdir
    #
    downloads = os.path.expanduser("~/Downloads")
    #changes the current working directory into the 'Downloads' folder
    #
    os.chdir(downloads)
    #assigns source to be a list of all the files in 'Downloads'
    #
    source = os.listdir(downloads)
    #scrolls through all the files in 'Downloads' to see if any 'endswith' '.ppt' or '.pptx'
    #
    for files in source:
        #print(files)
        #proceeds through the if statement if the file has the extension '.ppt' or '.pptx'
        #
        if files.endswith(".pptx") or files.endswith("ppt"):
            #uses 'shutil.copy' to copy the located file to the 'destination' which was defined earlier
            #
            shutil.copy(files,destination)
            #the print command below is used for debugging to see in the listed files where the match was found
            #print("-------------------")

#pptx_copy()
