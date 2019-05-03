# Wrangling Permissions
System administrators spend a lot of time managing user accounts. On the flipside, penetration testers spend a lot of time _breaking into_ user accounts. No matter which side you're on, a thorough understanding of how to configure user accounts is paramount.

For this assignment, you'll use your Ubuntu Virtual Machine.
- Create users and groups
- Set file permissions
- Manage `sudo` rights

---

## Instructions
### Part I: Users and Groups
- In your Virtual Machine, create the following user accounts:
  - `Andy`
  - `Ollie`
  - `Tina`
  - `Louise`
  - `Gene`
  - `Jimmy`
  - `Teddy`
- Set their passwords to be whatever you would like.
- Then, create the following groups with the following members:
  - `students`: Andy, Ollie, Gene, Jimmy, Teddy
  - `teachers`: Tina, Louise, Ollie
  - Add `Teddy` and `Louise` to the `sudo` and `adm` groups.

When you're done, run: `cut -d: -f1 /etc/passwd | xargs groups` and take a screenshot. This command will show all users, along with the groups they're in. **You'll submit this screenshot as proof of your solution.**

### Part II: Restricting Sudo Access
- Use `visudo` to update `/etc/sudoers` such that `Teddy` and `Louise` can _only_ run `apt` with `sudo`.

When you're done, run: `cat /etc/sudoers`, and take a screenshot. **You'll submit this screenshot as proof of your solution.**

## Part III: Logging Sudo Access Attempts
- Check if `rsyslog` is installed. If not, install it.
- Start `rsyslog`.
  - **Note**: Use the `service` command.
- Switch users to `Louise`, and do the following:
  - Use `sudo` to run `apt update`, but enter the wrong password.
  - Use `sudo` to run `apt update`.
  - Use `sudo` to run `cat /etc/passwd`.
- Repeat the above as `Teddy`.
- Now, switch to the `root` user. Inspect `/var/log/auth.log`. Look for messages about `sudo`. Which of the commands you ran as `Teddy` and `Louise` do you see in the logs?

### Part IV: Customizing User Directories
- Still logged in as `root`:
- Inside each user's `/home` directory, create the following folders:
  - `Documents`
  - `Downloads`
  - `Pictures`
  - `Videos`

- Set permissions for each user's directory to have full permissions for the associated user, read permissions for their group, and no permissions for the world.
  - For example, files in Teddy's directory should have permissions like: `rwxr-----`.

- Test your permissions by switching to one of the users, and attempting to read the other users' files. You should get `Permission denied` errors.
  - For example, switch to the user `Teddy`, and try to list files in `/home/jane`.

- Research `/etc/skel` to figure out how to avoid manually creating `Documents`, etc., directories for every user: <http://www.linfo.org/etc_skel.html>

- Update your `/etc/skel` with `Documents`, etc., directories. Then, create a new user with your name. Inspect the contents of your new user's `/home` directory to verify that your `/etc/skel` update works as expected.
