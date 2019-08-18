## SIEMs Day 2: Guided Practice - Using Tables to Display Events in Splunk
--------

## Instructions

-------

 Now it's your turn! In this Guided Practice you create a **table** and **label the columns** for a search.  This makes it easier to interpret the results in reports and dashboards.

The Guided Practice uses the **same log file** from the previous activity: `alert_json_000015.log`.  Please **DO NOT reload** it if you completed the exercise.

#### NEW SPL Command Alert

The search should remove all **duplicates** that are found.  This is a NEW command. Please use the Search Manual to see how to search for duplicates at https://docs.splunk.com/Documentation/Splunk/7.2.4/SearchReference/Dedup.

**Getting Started**

* Create a search that returns events for Snort rules starting with **122**.

* **Remove** any duplicate source or destination IPs.

* Create a **table** with the following **fields**:

    * protocol
    
    * rule
    
    * source and destination aps.

* Label the **columns** `Protocol`, `Rule`,`Source IP and Port` and `Destination IP and Port`.

* Congratulations...Activity Complete!  
