#!/bin/bash
read -p "whats the current year? " year
read -p "whats your name " name
echo "hello " $name
read -p "How old are you " age
echo  "you are " $age " years old"
echo  "It is currently "  $year
echo "you were born in " $((year - age))
echo 
echo
echo "you just ran the " $0 " from args.sh" 

