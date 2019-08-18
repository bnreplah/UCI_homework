SIEMs Day 3: Datasets
--------

## Instructions

-------

### Instuctions

In this activity, you will put together elements from last class lesson and then add some new ones.

The workflow for this project is to **create a dataset**, then **implement a search** and save it to a **new dashboard**. 

**NOTE:** 

* The Guided Practice requires the **tutorialdata.zip**.  This file was loaded as part of the **Warm-Up Activity**.  Please **DO NOT reload** it if you completed the warm-up exercise.

* This Guided Practice also requires the **Splunk Add-on Dataset**. It is in the **splunk-datasets-add-on_10.tgz** file.  

* Please see the installation instructions in the **Dataset-1.0-Use-InstalltheSplunkDatasetsAdd-on.pdf** file. 

* The Add-on is installed when the **Create New Table Dataset (green button)** is available in the Datasets window.

You will use a NEW search command called `contingency`. 

See documentation here: https://docs.splunk.com/Documentation/Splunk/7.2.4/SearchReference/Contingency


Let's get started.

Your organization has received complaints from some customers that there are problems accessing the website. Is this a network and/or software issue? We want to investigate how the webserver is performing with individual client browsers. 

1. Create a **new Dataset** named `Buttercupgames_Activity` from the **access_combined_wcookie** index and sourcetype list.

2. **Select fields** that will be used to investigate the issue. 

3. Next display the **Dataset in a Search**.

4. Now construct a `contingency search` that will record and analyze the relationship between **browser clients** accessing the website and the **return status** from the server.   

    * Hint the syntax is `contingency <field><field>` 

    * Hint: `append` the new `contingency` command to the datamodel search

5. Create a **new Dashboard** for the resulting `contingency table.`

    * Name it `Buttercupgames_Activity_Dashboard`

    * Select `Shared App`

6. Discuss with the class what you see in the contingency search results.


Congratulations...You finished!
