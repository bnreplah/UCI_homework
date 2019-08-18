##Activity: Upload Web Log into Splunk

### Instructions
	
Your turn! In this activity, you will be uploading a webserver log file into Splunk.  This is an important exercise, as you will be uploading various files into Splunk during the coming classes. 

Please ask your TAs for assistance if you require help.

**Getting Started**

If you do not already have the file, please download it to your virtual machine using this [link](Resources/tmp/access_30DAY.log).

* There are five steps to uploading a file into Splunk.  Use the **Back** button to return to a previous step and the **Next** button to continue the upload process.

	![Images/add-data-workflow.png](Images/add-data-workflow.png)

#### 1. Select Source 

* First, select the **Splunk>Enterprise** logo in the left-hand side of the web page. 

* Select **Add Data** icon.

* Scroll down to see the list of common data sources and select the **Upload** icon at the bottom of the page.

* Under **Select Source**, click **Select File** and browse to the location for the `access_30DAY.log` file.

* Select the `access_30DAY.log` file and click **Open**

	* The loading status bar reads **DONE** when the upload is complete.

#### 2. Set Source Type

Splunk automatically detects the **source type** for `access_30DAY.log` file, which is *access_combined_wcookie*.

* Please select **Next** in the workflow bar to assign the input settings.

#### 3. Input Settings 

In this next step, you will assign values for the default Host settings.

* Please leave the `Source type` and `Index` at their **defaults values**.

* Next, set the Host setting by selecting the **Segment in path** button and type `1` for the segment number.	

* Select **Next** in the workflow bar to review the configuration.

#### 4. Review 

* Review all the steps.  Your configuration should look like the following.

	![Images/add-data-splunk-9.png](Images/add-data-splunk-9.png)

* You can go back at any time to modify information if it is not correct.

#### 5. Upload the Log File into Splunk

* Select **Submit**  in the workflow bar and then **Start Searching** to view the events in the **New Search** window.

**Success!** The results confirm that the data in the log was indexed and that events were created.

**Please do not close the search window**. You will use it in the next activity.