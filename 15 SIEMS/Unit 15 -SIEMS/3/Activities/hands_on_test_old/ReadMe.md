## Guided Practice: Roles and Users (0:20)

**Note:**
You will need to use the `class_data_sheet.csv` file for this lab. 

Log onto your Splunk instance and complete the following:

- a. Create a new role called "Justice League". Allow the role "Justice League" to...
	- Delete by keyword
	- change own password
	- Run searches
	- Edit other roles
	- Do not allow inherited permissions

- b. Add a new user
	- Batman (Fullname: Bruce Wayne) and assign the role of Justice League. **Do not require a password change** on the first time that Batman logins. 

- c. Create a new alert that has a table showing all backup volume by week day. The table needs only two columns called `date_wday` and `backupvolume`. 

- d. Save this as a dashboard panel called `Daily backups`. 

- e. Create a new Dashboard called `Justice` 

- f. Add the `Daily backups` to the Justice dashboard.

- g. Edit the `Batman` user and make him an admin

- h. Log out of being the `Administrator` and log into `Batman`.

- i. Change the dashboard to the Justice dashboard. 
