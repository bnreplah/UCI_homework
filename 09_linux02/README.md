# Ping Sweep
You've picked up a lot of heavy-hitting tools this week. The big ones are:
- Command and brace expansions (`$()`, `{}`)
- For loops
- Flow control operators (`&&`, `||`, `;`)
- Redirection operators (`>`, `>>`, `<`, `<<`)

For homework, you'll study script arguments on your own. Then, you'll use everything you've learned to write a script that performs a ping sweep of a subnet.

This script will be challenging, but it's a very realistic example. It's useful to be able to write a basic ping sweep, but you could just as easily replace the `ping` command with an Nmap script to run an attack against a whole series of IP addresses. Think of this as a "starting point" for more complex scripts you'll write later for network troubleshooting, penetration testing, and other tasks.

Aside from that, it's a thorough review of everything you've learned this week. To finish the script, you'll need to combine the following tools:
- Script arguments to get an IP address from users
- A for loop to ping a series of IP address
- Redirection to manage error messages from `ping`
- Flow control operators to generate custom error/success messages

You can start on the **Guided Study** immediately. You'll need to wait until Saturday's class to tackle the **Ping Sweep** assignment.

## Instructions
This assignment is broken into two parts: **Guided Study** and the **Ping Sweep Challenge**.

The Guided Study consists of two exercises and associated readings. In particular, you'll study:
- Passing arguments to scripts
- Collecting user input with the `read` command

You'll use one of these techniques to build the Ping Sweep script, so you _must_ complete the Guieded Study before proceeding to the Ping Sweep challenge.

The Ping Sweep Challenge requires you write a script that performs a ping sweep of a subnet, given a routing prefix such as `192.168.1`. 

Find detailed instructions for each section below. As always, don't hesitate to reach out to your instructors (and classmates!) for help.

**Good luck!**

### Guided Study
#### Script Arguments
Recall that commands can have **arguments**. An argument is simply data that the command needs to run. For example, in the below snippet, `/etc/shadow` is an argument to `cat`.

  ```bash
  $ cat /etc/shadow
  ```

Shell scripts can have arguments, as well. For the sake of example, let's say you have a script called `check_reachable.sh`, which uses `ping` to checks that a machine is alive, given its IP address.

   ```bash
   $ ./check_reachable.sh 192.168.1.5
   Checking 192.168.1.5...
   192.168.1.5 is UP!
   ```

In this case, `192.168.1.5` is an _argument_ to `check_reachable.sh`. 

This means that the code in the script has to be able to use the IP address the user provides. Refer to `check_reachable.sh` below.

  ```bash
  #!/bin/bash

  echo "Checking $1..." 
  ping $1 2>&1 > /dev/null && echo "$1 is UP!" || echo "$1 is DOWN!"
  ```

In this script, `$1` refer to the IP adress the user passed. In other words, `$1` refers to the _first_ argument the user passes on the command line. Similarly, `$2` refers to the second; `$3` to the third; etc. 

So, if a user runs the following script:

  ```bash
  $ ./my_script.sh first second third
  ```

...Then `$1` is `first`, `$2` is `second`, and `$3` is third. For this reason, arguments are also called **positional parameters**—the variables you use to refer to them depend on their _position_ on the command-line.

---

The exercises below will give you practice using positional parameters in your own scripts. You'll find detailed instructions for each in their activity folders. Please read this page _before_ starting the exercises: <http://linuxcommand.org/lc3_wss0120.php>
- [First Steps with Script Arguments](1-ScriptArguments/README.md)
- [mkdircd](2-mkdircd/README.md)

### Ping Sweep Challenge
For this exercise, you'll write a script that
- Collects a routing prefix from a user, such as `192.168.1`.
  - This is like an IP address, but _without_ the last three octet.
- Ping every IP address on the `/24` subnet, e.g.: `192.168.1.1`; `192.168.1.2`; etc.

Running the script should look like:

  ```bash
  $ ./ping_sweep.sh 192.168.1
  Scanning 192.168.1.0/24...
  ---
  The following hosts are UP:
    192.168.1.2
    192.168.1.3
  These hosts have been saved to 'live_hosts.txt'.
  ---
  IP Addresses that are DOWN are stored in 'down_hosts.txt'.
  ```

Find detailed instructions in [3-PingSweep/README.md](3-PingSweep/README.md).

## Submission
Submit the following:
- Your solution to **Playing with Args** (a script called `args.sh`)
- Your solution to **mkdircd** (a script called `mkdircd`)
- Your solution to **Ping Sweep** (a script called `ping_sweep.sh`)
