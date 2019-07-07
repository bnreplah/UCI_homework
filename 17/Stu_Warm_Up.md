## Digital Forensics Day 2: Review of Autopsy
--------

## Instructions 

Welcome back! In this guided practice, you review the steps from Day 1 for creating a new case. We've added some new steps too. 

Please ask your TA for help if you need it.

### Get Started

1. Start VirtualBox.

1. Start the Kali Linux VM.

1. Open a terminal window.

1. Navigate to the `autopsy-files/autopsy-4.10.0/bin` directory.

1. Start Autopsy: ` ./autopsy`

1. Start a new case.

   * Here's the information for the new case:

	  * **Case name**: 2012-07-18-National-Gallery
	
	  * **Case number**: A123456
	
	  * The **image file** is the same as Day 1: *tracy-phone-2012-07-15.final.E01*
	
	 Additional Ingest Settings:
	
	  * **Extension Mismatch Detector**: Check all file types
	
	  * **Keyword Search**: Just select **URL**

1. Select **Finish**.

    * The files will now be analyzed by Autopsy. When this process is finished, the file is ready. This may take some time.   
		
    * The **progress bar** in the righthand area of the screen will indicate when the ingest is complete. 
				
1. When the ingest is complete, locate the **Encryption Detection** area in the Directory Tree and open the *documents.zip* file to view the data in the image.

1. The image starts with the **Directory Sources** tree.

1. In the tree, you will see *tracy-phone-2012-07-15-final.EO1*, which is the iPhone image file.
	
   * Don't worry if you do not understand everything in the image file. You'll learn more during the instruction and activities.
	
### Look at Tracy's Browsing History

This example shows how you can get to an evidence file without traversing the evidence tree. You just need to know the name of the file.

1. From the **Tools** menu, select **File Search by Attribute**.

1. Click the box next to **Name** and type **History.plist**.

1. Click the **Search** button.

1. Now select **History.plist** from the **Listing** pane.

1. Select the **Indexed Text** tab in the **Data Content** pane to see what Tracy's been up to.

### Look at File Metadata

Let's look at the file metadata. We need this information for our evidence reporting.

* Select the **File Metadata** tab in the **Data Content** pane to see the **md5 hash**, **creation date**, **file name**, and **location**.

* Great job finding your first pieces of evidence!



	