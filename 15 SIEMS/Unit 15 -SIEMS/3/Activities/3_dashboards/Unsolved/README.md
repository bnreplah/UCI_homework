## SIEMs Day 3: Guided Practice - Create a Dashboard for Failed Password Attempts
--------

## Instructions

-------

Welcome to the Activity! In this Guided Practice you will create a **Failed Password Dashboard** for monitoring login attempts on *Linux* and *Windows* systems for a SOC team. 

You will first create a report for the dashboard for monitoring a `Linux server`. Next, you will add the existing `Windows failed login` search to the dashboard. Finally, you will `edit` the dashboard for quick viewing by the SOC team. 

Please ask your TA for assistance if you need help. 

#### Getting Started

Your first task is to create a search to report **failed password attempts** from a Linux system log file. 

1. Start by uploading the `linux_s_30DAY.log` system log file into Splunk. 

2. Select **syslog** from the **Operating System** Source Type drop down list.

3. Continue with the upload.

4. Review the events from the log.

#### Create a Search and Report

5. Next, create a search that returns **ALL failed password attempts**.

6. Save the **search as a Report** with:
 
    * `Title` = **Linux Failed Password Attempts**   
 
7. Save and view the Report.

8. Locate the Report in the `Report List` and execute the search.

#### Create a New Dashboard for the Report
 
9. Now add the report to a NEW dashboard:
 
    * `Title` = **Linux and Windows Failed Passwords**

    * Complete the additional fields and save the dashboard.

10.   View the Report in the Dashboard.  

#### Add an Existing Report to a Dashboard

Your second task is to add the `Windows Event failed login` search from the Warm-Up exercise to  the **Linux and Windows Failed Password Reports** dashboard.

1. Locate the **Failed Login Search Report** in the **Report List**.

2. Add the report in the **Linux and Windows Failed Password** dashboard.

3. View the Dashboard in the **Dashboard List**.

#### Edit the Dashboard

1. Click the **Edit** button and enter **titles** for the dashboard panels: `Linux Login Event Log` and `Windows Event Log`

2. Drag the bottom panel so that the tables are **side-by-side**.

3. **Save** and redisplay the dashboard.

 **Congratulations...Activity is complete!**   

