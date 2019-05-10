#!/bin/bash
# sanity check:
echo "Hello World"

# print out $0
echo $0

# What does it contain ?
# The argument $0 contains the index value of 0 in the command line command being run:  bash thisscript.sh the $0 of this is bash or ./thisscript.sh the $0 is ./thisscript.sh


# print out $1
echo $1

# what happens when you rub the script _with_ arguments???
#it prints out the arguments run
# What happens when you run the script _without_ arguments???
#when run without arguments it prints out null

# Write a script that acceprs _three_ arguments from the user, then Prints out the following:
####### The name of the script
####### The value of each argument
./argument.sh

