# Submission

### Tar
#### Stripping Components
- **Exercise 2**
  - Extract `Movies`: tar xvf file.tar --strip=2 file/things/Movies
  - Extract `Movies/ZOE_0004.mp4`: tar xvf file.tar --strip=3 file/things/Movies/ZOE_004.mp4

#### Modifying Archives
- **Exercise 1**

  ```bash
  # Insert the solution commands for Exercise 1 below
    tar -Avf Update.tar sample.tar
    tar -tvf Update.tar
    touch test1.txt test2.txt
    tar -rvf Update.tar test1.txt test2.txt
    tar -tvf Update.tar
  ```

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
    tar -uvf Update.tar test1.txt
    tar -tlvf Update.tar
  ```

- **Exercise 3**

  ```bash
  # Insert the solution commands for Exercise 3 below
    tar --delete -f Update.tar test1.txt
    tar -tlvf Update.tar
  ```

#### Incremental Backups
- **Exercise 1**
  - A **snapshot file** is 'is a file created during incremental backups. This file contains the 
status of the files sytem at the time of the dump, determining which files were modified.'
	`tar --create --file=base.tar --listed-incremental=/var/log/usr.snar /usr`.
  - A **backup level** is 'the levels of modification since the initial commit. In full backups 
the back up levels remain in the range of 0-1 while one file is consistantly rewritten with all 
the new changed information of the current state of the computer. In incremental backups each 
level contaisnt the modified data from the last.'
	`tar --create --file=archive.3.tar --listed-incremental=/var/log/usr.snar /usr`.
  - A **level 0 backup** is 'is a backup containing a abckup fo all the details of the entire 
operating system'
	`tar --create --file=base.0.tar --listed-incremental=/var/log/usr.snar --level=0 /usr`.

- **Exercise 2**

  ```bash
  # Insert the solution commands for Exercise 2 below
    tar --create --file=base.tar --listed-incremental=/var/log/home.snar --level=0 /usr
    cp /var/log/home.snar /var/log/home.snar-1
    touch ~/new_file1.txt ~/new_file2.txt
    tar --create --file=archive.1.tar --listed-incremental=/var/log/home.snar-1 /usr
    tar -tlvf archive.1.tar
    cat home.snar
  ```

### Cron
#### Managing cron
Please paste the contents of `backup-cron-jobs.txt` in the space below.

  ```bash
  # Paste the contents of `backup-cron-jobs.txt` below
    echo "*/30 */6 */15 */6 0,6 echo running a cronjob >/dev/null 2>&1" >cronjob
    crontab cronjob
    crontab -l > backup-cron-jobs.txt
    crontab -ir 
    crontab backup-cron-jobs.txt
    crontab -l
  ```
