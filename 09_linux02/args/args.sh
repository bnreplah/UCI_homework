#!/bin/bash
# sanity check:
echo "Hello World"

# print out $0
echo $0

# What does it contain ?
# The argument $0 contains the current running command
# $0 is the standard input, thus the last thing inputed into the terminal. In this case it was './args.sh'

# print out $1
echo $1

# what happens when you rub the script _with_ arguments???
# What happens when you run the script _without_ arguments???

# Write a script that acceprs _three_ arguments from the user, then Prints out the following:
####### The name of the script
####### The value of each argument
./argument.sh

