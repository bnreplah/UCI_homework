#### Instructions

In this activity,  you will use the new `awk` syntax we have just covered in class, to parsing out data from the files and directories you received from the `Awk.zip` directory 

Using the `17-18-Breaches.txt` file, create various AWK commands that accomplish the following:

- Print only the first field of the 17-18-Breaches.txt.
awk '{print $0}' 17-18-Breaches.txt
- Print only the breaches from 'web' companies.

- Out of the web companies that were breached, print only the company name.

- Print all the breaches from 2017.

- For the companies that had breaches in 2017, print only the company names and the number of records lost.

- For the companies that had breaches in 2018, save the company name, company type and number of breaches to a new file named 2018Breaches.txt
awk '/2018/ {print $1 "/t" $4 "/t" $3}' >> 2018Breaches.txt
**Note:** If you get stuck, please raise your hand and one of the TA's will come by and help you. 