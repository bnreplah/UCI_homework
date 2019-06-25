## Direct Instruction: Visualization Activity Review (0:05)

- Poll students to see if they were able to complete the exercise

- Use the following steps to walkthrough the activity. 

**Step 1: Creating the Search**

  - To view the source of `fortinet_logs.csv` in a geographic visualization, search for
		
      `source="fortinet_logs.csv"   | iplocation src_ip  | geostats  count`
		
   - To add in the criteria the students could either type in the additional criteria or click on it on the left side of their search screen to add it in the search.  
	
	- Make sure to demonstrate how to search for a wildcard in the IP address by adding an asterisk.
	
	- Finally, display the complete search:
	
	   - `source="fortinet_logs.csv"  src_port=3430  dest_ip="195.*" | iplocation src_ip  | geostats  count`
	
**Step 2: Finding the Top Country**

   - Let students know there are a few ways to figure out the top country.  
   
   - The simplest method is clicking on the **Country Field** on the left of the `events` tab.  See the screen shot below.
   
   - Point out that the top country is the Republic of Korea.
   
      ![Resources/top_country.jpg](Resources/top_country.jpg)
	
**Step 3: Creating the Visualization**	

   - Select the visualization tab and make sure that `Cluster Map` is the selected visualization.
	
**Step 4: Zoom in on the Top country**	

   - Illustrate to  students how to drag over the map to South Korea, then select the `+` sign to zoom in on the country so that South Korea is the main country displayed in the visualization.  See the screen shot below on how it should look.
   
      ![Resources/korea.jpg](Resources/korea.jpg)
