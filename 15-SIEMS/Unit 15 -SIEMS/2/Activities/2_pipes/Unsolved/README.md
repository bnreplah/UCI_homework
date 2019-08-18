## SIEMs Day 2: Guided Practice - Using Pipes with Splunk
--------

## Instructions

-------

Welcome! In this Guided Practice you will practice using **pipes** in Slunk.

* You will work with the following file:

    * source = `alert_json_000015.log`. This file contains Snort alerts in  json formatted.

**Getting Started**

* Start by uploading the SNORT `alert_json_000015.log` file into Splunk.

* It is IMPORTANT to select **Structured** = **json_no_timestamp** for the `source type`.

* Continue with the file upload.

* When the upload is finished, review the **Interesting Fields** to determine what Snort `fields` can be used in the investigation.

    * Open fields `protocol`, `name`, `dest_ip`, `dest_port`,`src_ip`,`src_port`, `eventtype` and `severity` or `priority` to see their values. 

    Hint: Move these fields to **Selected Fields**.

* Scroll down and review the raw event data.  Do you recognize some of the fields?

### The Investigations

You will create searches for two investigations. As you work through each search think about the following:

  * What **fields** are required in the search?

  * What **operators** are required in the search (e.g., AND, OR, =)?

  * What **pipelines** are used in the search?

* Rmember that all results are located in the *Statistics* tab.  

* Hint: Use the **Matching Fields** area for help with entering field names and the **How to Search** for help correcting errors.

#### Part 1:

You are asked to investigate a number of **port scanning** alerts.

* Create a search that will find all alerts for port scanning activity. Display results for the top `destination IP addresses`. 

* Write out your search command. 

* Try it in Splunk!

* How many search results were returned from the top command?

* What where the `top three IP` address from the search?

* `View the events` for each IP.  What type of port scans were performed?


Now, narrow **this search** so that it only includes the `TCP port scans` for the `top five` source IP addresses. Show **ONLY the number** of search results.

* Write out your search command.

* Try it in Splunk!

* `View the events` for the first IP address.  

* `Locate` the `first` event.

* What `port` is being investigated at the `source IP`? How can this port be used? 
  
    Hint: See the **The Port Database** located at https://speedguide.net/ports.php 


#### Part 2:

Next, investigate alerts that indicate *remote code execution*. There is a **NEW SPL command** that is used in this search - `sort`.

* Find all instances of **remote code execution**. Narrow your search for all instances where the destination port is **445**. 

* **Sort** by the `destination IP` in `descending` order.

  * Hint: The `sort` command is located in **Search Commands** in the Search Manual https://docs.splunk.com/Documentation/Splunk/7.2.4/SearchReference/WhatsInThisManual

* What`priority` and `eventtype` is returned for this search?

* What are the `source IP` and `destination IP` addresses?
  
* Go to the `SNORT Sid database` and write down the details for the alert.

    * The database is located here located at https://www.snort.org/docs/.  Example search SID: `122-1`.

* How can `port 445` be used by an attacker?

* Congratulations...Activity Complete!  
