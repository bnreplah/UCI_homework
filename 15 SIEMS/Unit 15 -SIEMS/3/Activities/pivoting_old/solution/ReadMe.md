## Discovering Backups

In this lab, you'll need to create a pivot table showing all of the most recent backups. Please use the `class_data_sheet.csv` and build the pivot table as the following...

- 1. Create the Data model with the name `Backup`. Add the extracted fields...
	- a. backupduration
	- b. backupvolume
	- c. usr
- 2. Using Splunks different charts answer the following questions...

 **Questions**
-  1. Which user had the biggest backup volume?
-  2. Who had the smallest backup?
-  3. Whose back up took the longest?

---

## Solution:

- For this demonstration please make sure you are using the `class_data_sheet.csv`

- These solutions are written as if you put the host name as `datasheet.csv`

**Step 1: Dataset**

  - Click:`Settings`
  
  - Click: `Data Model`
  
  - Give it a title called: `Backups`
  
  - Click: `Root Event`
  
  - Type: `DataSet name = backups`
  
  - Type: `host= datasheet.csv` for constraints. 
  
  - Click: `Preview`
  
  - Click: `Save`
  
  - Click: `Add field`
  
  - Add: `Backup Volume` `Backup` `Usr`

**Step 2: Filters**
  
  - Choose: `All Time`

**Step 3: Split Rows**
  
  - Choose: `Usr`

**Step 4: Column Values**
  
  - Choose: `backupvolume`

  - Choose: `Column Chart`

**Questions**
   
 1. Which user had the biggest backup volume?
 	
    `aalvarez57`
   
 2. Who had the smallest backup?
	
      `ahunti2`
   
 3. Whose back up took the longest?
	
      Change the Y axis to `backupduration`
	
      `adunn2x`