## SIEMS Day 2:  Guided Practice - Warm-Up Exercise
--------

## Instructions

-------

- Welcome Back! In this Guided Practice you will prepare for a technical interview about using Splunk Enterprise.   

- Start by downloading the tutorialdata.zip file.  It will be used in the hands-on exercise.

#### Hands-on Exercise using the SPL to Execute Searches

You might be asked to demonstrate how to use SPL to perform searches related to **website performance** and **threat detection**.

To prepare you will use the **tutorialdata.zip** file from the Day 1 instruction on Interface and Data Sets. This file contains the machine data from the **buttercupgames** website. The site sells video games and simulations.

* Log into the Splunk Web Interface using `splunk` and `splunk`. 

* Execute the following searches specifying `All Time` for the time range.

* Explain **why** you are conducting each investigaton and **what** is returned in the search **events**.

Here are the four search commands.  They use wildcard, comparison and Boolean operators.

1. `sourcetype=access_* AND (status=500 OR status=404)`

2. `host=mailsv failed password`

3. `host=www* useragent=*`

4. `"?msg=Credit*" AND file="error.do" AND host!=www2`

Congratulations. You finished the interview.
