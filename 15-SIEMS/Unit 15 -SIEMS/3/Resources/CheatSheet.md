### Cheat sheet

- This is a hard week, because of this I have started this cheat sheet to help guide you along. Please always reach out if you have anyqeustions


## Setting up Forwarders on Ubuntu

- On the Ubuntu machine run:
	- `splunkforwarder/bin/splunk enable boot-start --accept-license` Allow to forward
	- `splunkforwarder/bin/splunk add forward-server <The Windows 10 IP Address>:9997` Set forwarder
	- `splunkforwarder/bin/splunk list forward-server` Check settings
	- `splunkforwarder/bin/splunk list start` Start the forward server

- On the Windows machine run:	
	- Go to `Settings`
	- `Forwarding and Receiving`
	- Enter the default port `9997`

- On the Ubuntu machine run: 
	- `splunkforwarder /bin/splunk restart` Restart the service
	- `splunkforwarder/bin/splunk list forward-server` Verify it's working
	- `splunkforwarder /bin/splunk add monitor /var/log` Watch all var logs

- On the Windows machine run:
	-  Go home
	- `Searching and reporting`	
	- `Data Summary`


## Searching
	
- `sourcetype=WinEventLog:Security EventCode=4625 user=* | timechart span=1h count(EventCode) by user`

- This is complicated so let's break this down...

`sourcetype=WinEventLog:Security EventCode=4625 user=*`
- I am searching for a specific source type. This source type was created by a Splunk App for Windows.
- The source type I am searching for is the `Security` portion of the `WinEventLog`.
- I am also narrowing my search to one specific event `code:4625`,which is a failed logon.
- Finally, I want to include all the `usernames` because I know I am going to use this field later to build a table or visualization.

*Next Part*
- `| timechart span=1h count(EventCode) by user`
-  I am ”piping”the previous data into a time chart command.
-  By using the `span=1hrstatement`,I am forcing the chart to have one hour increments. 
-  Next,I am counting the `EventCode`(which is what I searched for before the pipe).
-  Finally,I want the data analyzed by user.	