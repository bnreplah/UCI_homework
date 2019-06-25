## Pivoting non-gui

- In this lab, you'll need to create a pivot table without the GUI. Once again use the `class_data_sheet.csv` and build the pivot table as the following...

- 1. Create a report with the following variables...
	- a. Shows all and any users
	- b. Shows all and any states
	- c. Build a chart the counts the user by state
	- d. Rename state to "State" and count(usr) to "Number of Users"
	- e. Click on the visualization tab
	- f. Save this as a dashboard panel and add it to your dashboard
	
- 2. Answer the following questions...

 **Questions**
-  1. Which state had the most number of users? `CA with 237`
-  2. Which state had the least amount of users? `NH, RI, WY`

---

## Solution

- In the search enter the following (assuming you kept the host name as `class_data_sheet.csv` )

`host=class_data_sheet.csv usr=* state=* | chart count(usr) BY state | rename state TO State count(usr) AS "Number of Users"`

- Save as Dashboard Panel 

