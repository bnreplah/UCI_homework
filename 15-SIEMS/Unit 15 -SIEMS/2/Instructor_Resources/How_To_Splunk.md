## SIEM Day 2: How To Install Splunk
--------

## Instructions 

-------

1. Start by logging into the Ubuntu VM.	

    * username: `splunk`

    * password: `splunk`

2. Change to the `root` user and enter your password.

    * Run: `sudo su`

3. Now change to the **/opt** directory and **list** the contents.

	  * Run: `cd /opt`

    * Run: `ls`

    ![Images/tar-file-in-opt-dir.png](Images/tar-file-in-opt-dir.png)

4. Untar the tarball in the `opt` directory. 

	  * Run: `tar -xvf <name_of_tar_file>`

    ![Images/tar-file-command.png](Images/tar-file-command.png)
 
    * This creates a **splunk** directory.

5. Change mode on the **splunk** directory.

	  * Run: `chmod -R 777 splunk`

    ![Images/chmod-file.png](Images/chmod-file.png)


### Starting a Splunk Instance

6. Splunk is executed from the **opt/splunk/bin/** directory.

	  * Run: `cd /opt/splunk/bin/`

#### Starting after the Installation  

7. If you are starting splunk for the first time after installation you will be prompted for an administrator username and password.

	  * Run: `./splunk start --accept-license`

    * Enter an `administrator name`

    * Enter an `administrator password`

    ![Images/splunk-bin-start-admin-account.png](Images/splunk-bin-start-admin-account.png)
