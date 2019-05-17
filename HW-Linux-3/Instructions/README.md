# Linux 3
This week, you studied:
- Creating and compressing backups with `tar`, gzip, and bzip2
- Scheduling jobs with cron
- Logging and log analysis

For homework, you'll expand on what you learned by researching additional features of tar and cron. In particular, you'll learn about:
- **Incremental backups** with tar
- **Extracting individual files** with tar's `--strip-components` flag
- **Managing and backing up** cron files

You will have to complete a series of readings, exercises, and questions. **Please record your solution commands and answers to the questions in a text file for submission**. Use the template in [Submission.md](Submission.md).

---

## Instructions

### Tar
#### Stripping Components
By default, `tar` includes directory structures when you unpack archives. For example:

  ```bash
  $ tar -xvf TarDocs.tar "TarDocs/Movies"

  # Extracts `Tardocs/Movies`
  $ ls Tardocs
    Movies
  ```

If you _just_ want to extract the `Movies` directory, and _not_ `TarDocs/Movies`, you can use the `--strip-components` flag.

Work through the exercises below to understand `--strip-components`.

---

- **Exercise 1**
  - Run: `tar --help | less`. Search for `--strip-components`.

  - Read the article at: <https://www.gnu.org/software/tar/manual/html_section/tar_51.html>
    - Read up until the line: `The option --strip=2 instructs tar to...`

- **Exercise 2**
  - Use `--strip-components` to extract the `Movies` directory.

  - Use `--strip-components` to extract the `Movies/ZOE_0004.mp4` file.

#### Modifying Archives
You will often find yourself needing to add, remove, or update files from an existing tarball.

You can do this with the following flags:
- **Add files with** `-r`: `tar rvf <existing archive> <new filename>`
- **Update files with** `-u`: `tar uvf <existing archive> <updated file>`
- **Update files with** `-d` or `--delete`: `tar -f <existing archive> --delete <file to delete>`

Note that the `<updated file>` and `<file to delete>` must exist in `<existing archive>` for the above commands to work.

In these exercises, you will practice using these flags to update an existing tarball.

---

- Open a terminal window on the Virtual Machine.

- Change to the `Projects` directory.

- **Exercise 1**

  - Copy `sample.tar` to `update.tar`

  - List the contents of `update.tar`.

  - Create two files: `test1.txt` and `test2.txt`.

  - Append them to `update.tar`.

  - List the contents of `update.tar`.

- **Exercise 2**

  - Update `update.tar` with the latest copy of `test2.txt`.

  - List the contents of `update.tar`. Is the latest copy in the archive?

- **Exercise 3**

  - Delete `test1.txt` from `update.tar`.

  - List the contents of `update.tar`.


#### Incremental Backups
You'll often use `tar` to back up the same directories on a regular basis—e.g., you might back up `/home` every day at midnight.

We'll focus on two main backup strategies:
- **Full Backup**: Create a new backup from scratch. This is what you've been doing with `tar`. In this scenario, you'll back up _every_ file in `/home`, _every_ day. Full backups are safe, but slow, and take up a lot of space.
- **Incremental Backups**: Updates an existing backup with _only_ the files that changed. For example, if you back up `/home` on Sunday, and add a file called `/home/new.file` on Monday, the next backup will _only_ include `/home/new.file`. Since the other files didn't change, they won't be backed up. Incremental backups are fast, and each incremental backup is small.

A full backup is simply a tar archive. To restore it, you simply extract the archive.

Incremental backups are a little more complicated. You'll have one "base backup", such as `backup.tar`. This is a full backup of the file system you want to save. This is also your starting point. When you make incremental backups, `tar` will create small archives that _only_ contain the files that changed since you created `backup.tar`. So, you would end up with something like:

  ```bash
  $ ls -1 /var/backups
    base.tar
    # Contains files that changed from/weren't in `base.tar`
    incremental.1.tar

    # Contains files that changed from/weren't in `incremental.1.tar`
    incremental.2.tar
 ```

To restore from incremental backups, you need `base.tar`, _and_ every incremental backup up to the point of restoration.

A related skill is updating tar archives manually. This way, you can add/remove files to/from an archive on an _ad hoc_ basis.

For these exercises, you will create incremental backups with `tar`.

---

- **Exercise 1**
  - Read more about incremental backups at: <https://www.gnu.org/software/tar/manual/html_node/Incremental-Dumps.html>
    - What is a snapshot file?
    - What is a "backup level"? What is a "level 0" backup?

- **Exercise 2**
  - Follow the steps below:
    - Create a level 0 backup of `/home`.
    - Add two files to your home directory with:
      - `touch ~/new_file.1 ~/new_file.2`
    - Use `--list-incremental` to create a level 1 backup. Call your snapshot file `/var/log/home.snar`.
    - Copy `/var/log/home.snar` to `/var/log/home.snar-1`. You need this copy to create your level 1 backup.
    - List the contents of your level 1 backup, and read `/var/log/home.snar`. Do you see what you expect?

### Cron
#### Managing crontabs
It is **best practice** to keep backups of your cron table.  This ensures that there is a backup in case of accidental deletion.

To display and backup your crontab file, run:

  ```bash
  # Display crontab file
  $ crontab -l

  # Backup crontab file
  $ crontab -l > backup-cron-jobs.txt
  ```

You can remove a crontab file with the `-i` flag:

  ```bash
  # Removes your crontab file
  $ crontab -i

  # Prints: `no crontab for <"user">`
  $ crontab -l
  ```

To restore your cron table, run:

  ```bash
  # Restores your backup
  $ crontab backup-cron-jobs.txt

  # Prints the same cron table you starte with
  $ crontab -l
  ```

In the next exercise, you will practice writing commands using the **cron simulator** at https://crontab-generator.org to run on the Virtual Machine.

Using a simulator is a great way to validate existing cron statements or to create new ones. Using a tool like this is a good habit to get into.

---

**Part 1: Practice**

  * Working in your `home` directory, launch the nano editor:  `nano cronsim.txt`

  * Open a web browser on the Virtual Machine and navigate to https://crontab-generator.org.

  * Practice by creating three cron jobs:

      * Schedule the jobs using the **Minutes, Hours, Days, Months and Weekday** radio buttons.

      * Enter a command in the **Command to Execute** field. Go for it! Enter any command you've learned from previous activities.

      * Select **Mute the Execution (Don't save or send output)** radio button.

      * Select the **Generate Crontab line** button to see the statement.

      * View the output and **copy each line** into your text file.

  * `Save` the file and `exit` the editor.

- **Part 2: Schedule a job to run in your crontab file** on the Virtual Machine.

  * First, return to your `~/Projects/TarDocs` directory.
    - Copy the contents of `~/Projects/TarDocs/Documents` into a `~/data/cron/Documents` directory.

  * List the contents of the directory.

  * Now let's look at what the cron job will do. You'll use many of the commands from previous activities.

  * The cron job should create a `cronjob.tar` tarball that contains **ONLY** the `text files` in the `~/data/cron/Documents` directory.

  * The job should then `untar` the tarball into a `data/cron/exercises` directory.

  **Suggestion**: Try each part (`tar`, `untar`) of the command in a terminal window to make sure they work.

  * Using the simulator schedule the job to run:

      * **Tue, Thu and Sat** - Note: some systems will not accept numbers.  Please use the names of the days.

      * **Every 2 minutes**

      * The cron job is a `single` line.

  * Copy the generated line into your crontab file.

- **Part 3: Check the output from your Job**

  * Check the `data/cron` directory for the `cronjob.tar` file.

  * Check the `exercises` folder for the extracted directory.


- **Part 4: Disable and Backup**

  - Disable all the cron jobs from the lesson activities in your crontab.

  - Backup the file to `backup-cron-jobs.txt`.

## Submission
Please fill out and submit the template in [Submission.md](Submission.md).
