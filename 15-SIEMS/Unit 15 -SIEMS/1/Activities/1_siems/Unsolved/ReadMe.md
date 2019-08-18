## Working with Logs and Events Activity File

#### Instructions 

Welcome to the second activity! This activity is comprised of three parts: 

First, we will assess your knowledge of SIEMS with mock first-round interview questions. 

Next, there is a hands-on exercise that involves basic normalization (parsing, identifying and labeling). This will assist you in recognizing and using field data (e.g., destination IP address) in Splunk.

The last exercise assesses your understanding of rule-based correlation techniques using pseudo-code statements. This exercise will prepare you for executing queries on event data using the Search Processing Language (SPL) and how to use SPL in security investigations. The SPL is similar to SQL.

Let's get started.

**Part 1: Interview Questions**

You are preparing for your first round of interviews with a company.  This interview will include assessing your knowledge of SIEMs. Prepare by answering the following questions:

1. List two benefits of using SIEMS.

2. How are logs used in a SIEMS? 

3. What is a baseline and how is it used in a SIEMS?


**Part 2: Normalization**

 In the lesson, we saw that a SIEMS collects *raw* logs and maps elements such as *source IP* and  *destination IP* to produce names for event types. 

 Think back to when we first dealt with log files in our Intro to Linux week: those log files were confusing and difficult to read. In this exercise, you are given a **web log** and asked to develop **fields names** for the elements in the log, so that data is **labeled automatically** by the SIEMS.

* Here is a sample log entry:

	```bash
    192.188.106.240 - - [06/Feb/2019:23:59:45] "GET http://www.buttercupgames.com/category.screen?
    categoryId=TEE&JSESSIONID=SD2SL4FF9ADFF4959 HTTP 1.1" 200 2958 
    ```

1. Research and review the format for a **HTTP GET** request to and response from a web server.

2. Now using your research, identify **the fields** in the HTTP log entry.

3. Select descriptive names for the **fields** that will automatically identify the parts of the log entry in the SIEMS.

4. Record your answers as:

	* field name = *value*

	* **HINT**: *htp_method = Get* 
		
		field name is *http_method*

		value is *GET*

**Part 3:**

Your next task is to investigate *unsuccessful* **GET responses** from the webserver for a **certain IP address** on a **particular date**.

* You will use the **log example from Part 2**.  Write a pseudo-code statement(s) that checks if the GET request to the server was unsuccessful for the source IP address and date in our sample log entry. 

* No need to get fancy with the code here, just explain what **fields** and **values** are required in plain English. Please use the field names you developed in Part 2 in your answer.

* **EXTRA CHALLENGE:** Send an alert if the count of unsuccessful GET responses are greater than 50 in one minute.