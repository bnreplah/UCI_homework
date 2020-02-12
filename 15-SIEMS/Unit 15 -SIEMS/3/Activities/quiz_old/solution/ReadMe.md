### Quick Quiz

Which port is the default forwarding port for the forwarder?
- 9907
- 8080
- 8089
- **9997**

Which port is the default management/deployment port?
- 9907
- 8080
**- 8089**
- 9997

Which type of forwarder requires a specific type of license?
- Light
- Advanced
**- Heavy**
- Universal

True or False: Machine data is only generated by web servers.
- True
- **False**

Some syslog devices do not require Splunk forwarders. Syslog data is generally received on port
**- 514**
- 80
- 8080
- 22	

True or False. Pivots can be saved as dashboards panels.
- **True**
- False


Which of the following is not a Splunk default metadata assignment?
- Host
- Source
- Index
**- Network**

Splunk can locally monitor both individual files an entire directories
**- True**
- False

Splunk can be set up in a distributed environment
**- True**
- False

Splunk can receive data from all of these except...
- Linux
- Mac
- Windows
**- Actually i'm pretty sure it can accept data from all of them.**

Splunk can be used to
- Investigate
- Alert
- Build Dashboards
**- All of the above**

True or False: I can install Splunk Enterpirse (not forwarder) onto a Linux box
- **True**
- False


True or False: Search terms are not case sensitive
- **True**
- False

After search query is entered, matching results are displayed in ___________ order.
- Chronological
- **Reverse Chronological**

Search results can be shared. (T/F)
- **True**
- False

Which of the following formats can search results **not** be exported into?
- CSV
- JSON
- XML
- PDF
- All the above

True or False: Machine data is always structured.
- True
- **False**

Splunk uses ________ to categorize the **type** of data being indexed.
- **Source**
- Host
- Timestamps
- JSON

True or False: The monitor input option will allow you to continuously monitor files.
- **True**
- False

Files indexed using the the upload input option get indexed _____.
- **once**
- continuously monitored

Would the ip column information be removed in the results of this search? `sourcetype=a* | rename IP as "User" | fields - ip`

- Yes, only users would show
- Yes, because it's being renamed
- No, it's just been relabeled as something else
- All of the above

- Written question: What would the following searches do? 

- `src="10.9.165.*" OR dst="10.9.165.8"`
- `source=job_listings salary>80000`
-`(code=10 OR code=29) host!="localhost"`
- Which app comes preinstalled with Splunk Enterprise?
- Finish the rename command to change the name of the status field to HTTP Status. sourcetype=a* status=404 | rename _______
- The knowledge objects that provide the data structure for pivot are called ____



































