## SIEMS Day 3: Warm-Up Activity - Investigate Failed Logins using the Contingency Commmand
--------

## Solution

--------

This activity showed how to use a `contingency table` to continue the *analysis of failed login attempts* to a web application.  Students developed a SPL command that looked at the relationship between `failed login attempts` and `account names` and `account domains` in a Windows event log.

* Poll students to see if they were able to complete the exercise.

* Tell students that `contingency tables` can be used to detect abnormal activity.

* Explain that the `locked` search uses a pipe with the `contingency command` to gather the search results.

    ![Images/contingency-locked-account.png](Images/contingency-locked-account.png)

   `source="wineventlogs_baseline.csv" host="splunk-VirtualBox" sourcetype="csv" "locked" | contingency Account_Name Account_Domain`

* Point out that the table narrows down the data to display the `top` username and domain and the number of locked events.  

* * Ask students *Where was the attacker trying to gain access?*

   *  **Answer:** Using `user_f` and `Domain_E` which showed `57 locked` events.

* Give another example of where a `contingency table` can be used such as **HTTP category and user agent** analysis.  This displays different browser agents and the return codes from a websever to monitor performance.

    ![Images/contingency.png](Images/contingency.png)

* Answer any questions the students may have before proceeding to the next section.
