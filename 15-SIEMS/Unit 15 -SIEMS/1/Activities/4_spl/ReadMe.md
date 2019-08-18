## Activity: Introduction to SPL

### Instructions

- Welcome to the last activity! In this activity, you will practice writing and implementing one search using the Search Processing Language (SPL).  

#### Part 1: Getting Started

First, answer these questions about Splunk and SPL.

1. What is an event?

2. What is a source type?

3. What is the most important search parameter to specify?

4. Identify what this SPL statement will do:

	```bash
		src="10.9.165.*" OR dst="10.9.165.8"
	```	

#### Using SPL to Retrieve Events

In this next exercise, you will retrieve events using the `access_30DAY.log`.

**Note:** Please select `All Time` in the **Time Picker**.


#### Part 2: Investigation

The customer support team at the Buttercupgames web site are receiving complaints that some customers are receiving *HTTP version not supported* responses from the webserver. Your task is to report on which browser are receiving the errors.

For the search write: 

1. The `field and corresponding value pairs`.

2. The `Boolean operator`.

3. Enter the resulting `search term` using SPL in the Search bar and execute the search.

#### Part 3: Narrowing down the search

* Start by specifying the following SPL in the Search bar so that ALL events are displayed:

	```bash
		source="access_30Day.log" sourcetype="access_combined_wcookie"
	```	

1. Write the search term that will first display events for ALL *server response errors*.

	**Hint:** Use the Internet to find the HTTP family of return codes.

2. Narrow your search down to the *HTTP version not supported* events.	

3. Isolate the *highest client software* that is originating the response.

	**Hint:** Use `Interesting Fields` to find the field that contains this value.

4. Record the number of events that are returned. 

5. Record the peak times when the events occur.

**Activity Complete!**
