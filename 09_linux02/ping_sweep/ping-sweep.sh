
#!/bin/bash
#user passes an incomplete ip
dev/null > live_hosts
dev/null > down_hosts
PREFIX=$1
#echo "Scanning loop $PREFIX.0/24..."
#seq 1 5
#for i in $(seq 0 24);
#	do echo $PREFIX.$i;
#done;

#updated loop:
echo "Scanning loop $PREFIX.0/225..."
seq 1 5
for i in $(seq 0 225);
do

#echo $PREFIX.$i
TARGET=$PREFIX.$i
#echo $TARGET
#
#ping -c 1 "$TARGET"  &&  echo "Target is UP" || echo "Target is DOWN"
#
#
#
#ping -c 1 "$TARGET" > /dev/null;
if !(ping -c 1 "$TARGET" 1> /dev/null)
then
	echo $TARGET " is DOWN"
	echo $TARGET >> down_hosts
#ping -c 1 "$TARGET"  &&  echo "Target is UP" || echo "Target is DOWN"
elif (ping -c 1 "$TARGET" 1> /dev/null)
then
	echo $TARGET " is UP"
	echo $TARGET >> live_hosts
#ping -c 1 "$TARGET"  &&  echo "Target is UP" || echo "Target is DOWN"
fi;
done
echo "#######################################"
echo "#######      Down Hosts         #######"
cat down_hosts

echo "#######################################"
echo "#######      Live Hosts         #######"
cat Live_hosts
