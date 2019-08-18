## SIEMs Day 3: Guided Practice - Create a Dashboard for Failed Password Attempts
--------

## Solutions

-------

Here are the solutions to the exercises.

### Getting Started

1. Start by uploading the `linux_s_30DAY.log` file into Splunk. 

2. Select **syslog** from the **Operating System** Source Type drop down list.

     ![Images/linux-30Day-upload.png](Images/linux-30Day-upload.png)

3. Continue with the upload.

4. Review the events from the log.

### Create a Search and Report

5. Next, create a search that returns ALL failed password attempts.

     **Answer:** Attach `Failed Password` to the SPL search command.

      ![Images/failed-password-attempts.png](Images/failed-password-attempts.png)

6. Save the **search as a Report** with:
 
    * `Title` = **Linux Failed Password Attempts**    
               
      ![Images/failed-password-attempts-1.png](Images/failed-password-attempts-1.png)


7. Save and view the Report.

     ![Images/failed-password-attempts-2.png](Images/failed-password-attempts-2.png)

8.  Locate the Report in the `Report List` and execute the search by selecting **Open in Search**. 

     ![Images/failed-password-attempts-3.png](Images/failed-password-attempts-3.png)

### Create a New Dashboard for the Report
 
9. Now add the report to a NEW dashboard:

     ![Images/failed-password-attempts-4.png](Images/failed-password-attempts-4.png)
 
     * `Title` = **Linux and Windows Failed Password**

     * Complete the additional fields and save the dashboard.

10. View the Dashboard in the Dashboard List. 

   ![Images/failed-password-attempts-5.png](Images/failed-password-attempts-5.png)


### Add an Existing Search to a Dashboard

The second task was to add the `Windows failed login` search to the **Linux and Windows Failed Password Reports** dashboard.

1.  Review how to find the **Failed Login Search Report** in the **Report List**

   ![Images/failed-login-save-as-report-4.png](Images/failed-login-save-as-report-4.png)


2. Add the report to the **Linux and Windows Failed Password** dashboard.

 ![Images/failed-password-attempts-6.png](Images/failed-password-attempts-6.png)


#### Edit the dashboard 

1. View the Dashboard from the **Dashboard List** and click the **Edit** button. 

   ![Images/failed-password-dashboard.png](Images/failed-password-dashboard.png)  


2. Enter **titles** for the dashboard panels: `Linux Login Event Log` and `Windows Event Log`

3. Drag the bottom panel so that the tables are **side-by-side**.

    ![Images/failed-password-attempts-9.png](Images/failed-password-attempts-9.png) 

4. **Save** and redisplay the dashboard.
  
* Answer any questions the students may have before going to the last topic for the course. 

