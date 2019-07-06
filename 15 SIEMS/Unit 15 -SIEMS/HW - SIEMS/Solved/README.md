Write down **each part** of the search and then try it in Splunk.

1. Upload **buttergames_email_log.csv** into Splunk.

2. Locate the fields of interest in **Interesting Fields** and place them in **Selected Fields**. For example **incoming_address, time**.


## Create the Search 

The search has three parts:

**Part 1:** 

* First, create a search where the Sender is *anyone* from @buttercupgames.com but the incoming IP address is NOT in the domain.

	* Hint: This section uses a `wildcard` and `relational operator`.

	* Try it in Splunk.
```	
	NOT incoming_address="10.*.*.*" Sender="*@buttercupgames.com"
```
**Part 2:** 

* Now locate emails that satisfy the criteria for suspicious emails. Here we will use the **stats** command with the *earliest* and *latest* times *by* incoming IP address. 

	* Hint: This uses a `pipe` command.

	* Try it in Splunk.
```	
	| stats count by _time, incoming_address | sort-_time desc
```
	* How is the time displayed?
```
	time is displayed in epoch time and in sort it is converted to human readable format.
```	
	* Check the earliest time value = `1483511846` at https://www.epochconverter.com/
```	 
	 1/4/2017 6:37 GMT 
```	
**Part 3:** 

* We are now in the last part of the search.  Place the output of the **stats** command in a **table** showing the `incoming IP address`, and the `earliest date/time` and `latest date/time` in human-readable form.

	* Hint: *convert* the earliest and latest time using the *ctime* command.

```
|ctime(_time) as Time
```

	* Try it in Splunk.
```	
	| table Time incoming_address
```
	* How is the time displayed?
```
	Time is displayed in human readable fromat in descending order
```	
Now look at the results and collect information for the incident report.
	
* What **incoming IP address** was used in the attack? 

```
74.207.253.34
```

* Click the suspect `incoming IP address` in the Statistics Table and select **View Event** until the event is displayed.


*  Who was the **Sender** in the Phishing attack?

```
address15@buttercupgames.com
```

*  Who was the **Recipient** of the attack?
```
address37@buttercupgames.com
```

*  What was the **Subject** of the email?

```
Anonymized Phishing Subject 19
```
	
*  What is the **Time** of the event?

```
2/1/17 4:29:19.000 AM
```
	
*  Where there any **Attachments**?

```
no
```
	
## Create a Cron Alert

We can monitor for `phishing attacks` with Splunk by scheduling alerts as a `cron` job.  

Please create a `scheduled cron alert` for the phishing search **which runs every five minutes**.

Review **Linux Day 2** on the `cron command` if you need a refresher on cron syntax. 

* First, run the `phishing` search and select Save as `Alert`.

Configure the alert as follows:

* Title: `Phishing Alert`

* Description: `This alert runs as a cron job every five minutes.`

* Permission: `Shared App`

* Alert Type: `Scheduled`, `Run on Cron Schedule`

* Time Range: `All Time`

* Cron Expression:  *Here enter the cron command to run every 5 minutes*.

* Trigger Conditions: Keep defaults

* Trigger Actions: 

	* Add Actions `Add to Triggered Alert`

	* Severity = `Critical`

* `Save` the Alert	

### View the Alert

* View the Alert from the **App** bar

### Trigger the Alert

* Run the search - select `All Time`

* Check the `Activity -> Triggered Alert` list.

### Disable the Alert 

* Disable the Alert after 10 entries.


Congratulations ....Homework Complete!	






