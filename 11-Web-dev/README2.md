# Setting Up a Web Application

In this homework, you'll use the LAMP server you built in class to serve a real web application. In particular, you'll use it to serve a _vulnerable_ web application, called DVWA. 

Soon, you'll use DVWA to study web vulnerabilities. Setting it up from scratch will help give you thorough context on how these vulnerabilities affect the underlying host.

Use the LAMP server you built in class as a starting point for this assignment.

**Good luck!**

## Instructions

### Downgrading PHP

In order for DVWA to work properly, we need to downgrade PHP on the LAMP server from php7 to php5.6

List all PHP packages and remove all unneeded 
- `sudo apt-get purge $(dpkg -l | grep php| awk '{print $2}' |tr "\n" " ")`
- Type `Y` and press enter

Add in repository
- `sudo add-apt-repository ppa:ondrej/php`
- Press `Enter`

Update the repository
- `sudo apt-get update`

Upgrade the repository
- `sudo apt-get upgrade`
- Type `Y` and press enter

Install php5.6
- `sudo apt-get install php5.6`
- Type `Y` and press enter

Install PHP modules
- `sudo apt-get install php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-xml`
- Type `Y` and press enter

Check php version is php5.6
- `sudo php -v`
- - You should see PHP 5.6 in the output

Restart apache2 service
- `sudo service apache2 restart`

Test apache by going to `http://localhost`

### Check PHP version Apache is using is php5.6

Since you downgraded to php5.6 above, lets check and make sure it installed properly

- `sudo a2enmod php5.6`
- Look for the phrase: **Module is already enabled**

### Getting DVWA

You'll get started by downloading the files needed to run DVWA.
- `cd /var/www`
- `sudo wget https://github.com/ethicalhack3r/DVWA/archive/master.zip`

### Download Unzip

Unzip is needed to unzip (extract) the DVWA ZIP file

Download and Install Unzip
- `sudo apt-get install unzip`

Unzip the Unzip ZIP file to /var/www/html
- `sudo unzip master.zip -d html/`

Rename DVWA-master folder to dvwa
- `cd /var/www/html`
- `sudo mv DVWA-master dvwa`

Rename DVWA config file.
- `sudo mv config/config.inc.php.dist config/config.inc.php`

### Open the DVWA Setup Page

Go to the DVWA setup page below to ensure the page comes up correctly

- `http://localhost/dvwa/setup.php`

### Correct some of the DVWA Setup page errors

As you can see from this page, there are some items in red that need to be corrected. Follow the steps below to correct those errors before creating the database.

Allow url includes
- `sudo nano /etc/php/5.6/apache2/php.ini`
- In nano, press `Control + w` key and type `allow_url_include` and change from `Off` to `On`.

Restart apache2 service
- `sudo service apache2 restart`

Install php-gd
 - `sudo apt-get install php5.6-gd`

Restart apache2 service
- `sudo service apache2 restart`

Edit the group and permissions of specific DVWA folders and files
- `sudo chgrp www-data hackable/uploads`
- `sudo chgrp www-data /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt`

- `sudo chmod g+w hackable/uploads`
- `sudo chmod g+w /var/www/html/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt`

Restart apache2 service
- `sudo service apache2 restart`

Check DVWA Setup page
- Go to `http://localhost/dvwa/setup.php` and make sure some of the items in red are now corrected based on the steps above.
- Do not worry about the CAPCHA items, that can be ignored.

### Configuring the Database

The DVWA config file asks for a MySQL username and password. Since one isn't setup yet, we are going to create  a user and grant that user privilages to the dvwa database we will be creating later.

Create MySQL username and password
- `CREATE USER dvwa@localhost IDENTIFIED BY 'abc123' ;`
- `GRANT ALL PRIVILEGES ON dvwa.* TO dvwa@localhost ;`

Update mysql section in the DVWA config.inc.php file
- `sudo nano /var/www/html/dvwa/config/config.inc.php`
- Edit the Mysql username to `dvwa` and password to `abc123`
- Save and exit config.inc.php file

### Creating the Database

Since we have the MySQL username and password created along with the permissions set for the user, we can now create the MySQL database for DVWA.

- Go to `http://localhost/dvwa/setup.php`
- Click **Create/Reset Database** button at the bottom. If successful, you will see output showing the database was successfully created at the bottom.
- If the database was successfull created, and if the page doesn't automatically redirect you, go to the `http://localhost/dvwa/login/php` page and login using the following default credentials:
 - username: `admin`
 - password: `password`

## Submission
When you're done, submit the following files in a tarball:
- `/var/www/html/config/config.inc.php`
- Screenshot of the DVWA welcome page after you succcessfully login
