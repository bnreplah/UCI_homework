# Setting Up a Web Application

In this homework, you'll use the LAMP server you built in class to serve a real web application. In particular, you'll use it to serve a _vulnerable_ web application, called DVWA. 

Soon, you'll use DVWA to study web vulnerabilities. Setting it up from scratch will help give you thorough context on how these vulnerabilities affect the underlying host.

Use the LAMP server you built in class as a starting point for this assignment.

**Good luck!**

## Instructions

### Getting DVWA
You'll get started by downloading the files needed to run DVWA.
- Install `git` on your Ubuntu machine.
- Move into `/tmp`, and run: `git clone https://github.com/ethicalhack3r/DVWA`.
  - This downloads a folder called DVWA to your `/tmp` directory.
- Move `/tmp/DVWA/dvwa` to `/var/www/html`.
- Open a browser and navigate to: `http://localhost/dvwa/setup.php`. You should see a setup page!

### Configuring the Database
To set up the database, you'll need to update one of DVWA's configuration files.
- Copy the file in `/var/www/html/dvwa/config/config.inc.php.dist` into `/var/www/html/dvwa/config/config.inc.php`.
- Use nano to update the database configuration in the top of the file. You'll need to:
  - Change the server IP address to `localhost`
  - Update the MySQL password with the one you set when configuring your LAMP stack

### Configuring PHP
To fully enable all the vulnerabilities in DVWA, you'll need to update your system's PHP configuration.

The bottom of the DVWA setup page provides information about which PHP modules are enabled vs which are disabled. For example, you need `allow_url_fopen` to be enabled for the application to work properly.

Refer to the configuration file here for the correct syntax: <https://raw.githubusercontent.com/ethicalhack3r/DVWA/master/php.ini>

- Find your `php.ini` file.
  - **Hint**: Use Google to look up the default location of this file.
- Use nano to turn on `allow_url_fopen` and `allow_url_include`.

## Submission
When you're done, submit the following files in a tarball:
- `/var/www/html/config/config.inc.php`
- Your `php.ini`
