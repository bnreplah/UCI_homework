## SIEMs Day 2: Guided Practice - Using Alerts to Monitor System Files
--------

## Instructions

-------

Welcome to the Activity. In this Guided Practice you will create a search that monitors errors in the internal Splunk log at `/opt/splunk/var/log/splunkd.log` and create an alert.

**Getting Started**

1. Start a new search.

2. Enter the following search in the Search window:

    ```bash
    index=_internal " error " NOT debug source="*splunkd.log"
    ```
    * As you type the command a notice appears that indicates this is a *savedsearch*.

3.  Select the link `splunk errors last 24 hours`and the search string will auto complete.
    
4. Set the Search Period to `All Time`.

5. Click the search icon to run the search.

#### Saving as Alert

Now save the search as an alert.

1. Select `Alert` from the `Save As` drop down list. 

2. Use the following values to populate the fields:

    * `Title` as **Error log from splunkd.log**

    *  `Permissions` as **Shared in app**

    *  `Alert type` as **Real-time**

    * `Trigger alert when` as **Per Result**

    * `Add Action` as **Add to Triggered Alerts -> Info** 

4. Click Save.  

5. Click Triggered Alerts to see the alerts.

 #### Triggering a Failed Login Attempt Alert

Trigger a failed login alert by logging into Splunk with an incorrect username and password (twice).  

#### View the Alerts in the Triggered Alert List

1. View alerts from the **Alert Menu**.

2. View alerts from the **Activity** drop down list

Congratulations ... The Activity is complete.
