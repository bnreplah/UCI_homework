## SIEMS Day 3: Warm-Up Activity - Investigate Failed Logins using the Contingency Commmand
--------

## Instructions

--------

Welcome to the Warm-up Activity!  

Your task was to monitor a web application where customers can purchase your company's products. You are concerned that there is a threat of an attacker attempting to **brute force login** to your application. 

Your search discovered that the Windows event log showed **57 failed login** attempts occurred in one minute. Using this data, you developed a `baseline` and `threshold` for creating alerts for `failed login attempts` to the web application.  

Your next task is to investigate the **target for the activity** by looking at the `account names` and `account domains` for failed login attempts in the Windows event log.

In this Warm-Up Exercise, we introduce a new SPL command that will help you with the investigation.
 
 The syntax for the command is: 
 
 `contingency <field><field>` where:

 - `contingency` is the Splunk command

 - `field` is a field in the event

  [Documentation](<https://docs.splunk.com/Documentation/Splunk/7.2.5/SearchReference/Contingency>) is available for the command at the Splunk website.  


#### 1. Getting Started

* Log into Splunk using your `username` and `password`.

* Upload the `wineventlogs_baseline.csv` file into Splunk.

#### 2. Execute a search for failed logins

* Next, write a SPL command that will search for `failed logins`.

#### 3. Investigate the target for the activity

* Now write a `contingency search` command that will display the relationship between `account names` and `account domains`.  This will narrow down the targets for the failed login attempts.

   * Hint: `pipe` the command to your first one.

 #### 4. Answer the following question  

* Where was the attacker trying to gain access?

Great job.  Activity Complete!