### Direct instruction: Review Roles and Users (0:10)

**Note:**
You will need to use the `class_data_sheet.csv` file for this lab. 

Log onto your Splunk instance and complete the following:

- a. Create a new role called "Justice League". Allow the role "Justice League" to...

	- Click: "Settings"
	- Click: "Access Controls" under the "Users and Authentication" section
	- Click: "+ Add new" on the Roles row
	- Type: "Justice" as the name
	- Choose the following for each capability
		- delete_by_keyword (Delete by keyword)
		- change_own_password (Change own password)
		- search (Run searches)
		- edit_roles (Edit other roles)
		- (Do not allow inherited permissions)

- b. Add a new user
- Batman (Fullname: Bruce Wayne) and assign the role of Justice League. **Do not require a password change** on the first time that Batman logins. 

	- Click: `Settings`
	- Click: `Access Controls` under the `Users and Authentication` section
	- Click: `+ Add new` on the Users row
	- Type: `Batman` for the name
	- Type: `Bruce Wayne` for the fullname
	- Assign: `Justice League` as the role
	- Uncheck: Require password change on first login

- c. Create a new alert that has a table showing all backup volume by week day. The table needs only two columns called `date_wday` and `backupvolume`. 

	- Upload the data `class_data_sheet.csv`
	- Use the search parameters `source="class_data_sheet.csv" fail* | table date_wday backupvolume`

- d. Save this as a dashboard panel called `Daily backups`. 
	- Click save as "Dashboard Panel"
	- Edit the permissions so everyone can read the panel
	
- e. Create a new Dashboard called `Justice` 
	- Click on "Dashboards"
	- Create New Dashboard
	- Give this dashboard the name Justice
	
- f. Add the `Daily backups` to the Justice dashboard.
	- Choose the Daily Backups panel
	- Click `Add to Dashboard`
	- Click `Save`

- g. Edit the `Batman` user and make him an admin

	- Click: "Settings"
	- Click: "Access Controls" under the "Users and Authentication" section
	- Click: Batman
	- Click: Justice League
	- Click: admin

- h. Log out of being the `Administrator` and log into `Batman`.
	- Click `Log Out`

- i. Change the dashboard to the Justice dashboard. 
	- Click `Choose a home dashboard`
	- Choose `Daily Backups`
