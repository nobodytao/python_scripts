<b>debian_workstations</b>

A simple task created while learning Ansible. It's made to control several virtual computers that use Debian 12.

Here's what it does:

- On the computers, it runs some basic commands like "whoami," "ip -a," and "free -m."
- The results of these commands are shown on the main computer screen using a special tool.
- It also makes a new folder called "./ansible/reports/" on the computers.
- Inside that folder, it creates text files with the names of the commands and the computer's IP address.
- These text files store what happened when those commands were run.
- There's also a file called "server-report.html" in that folder.
- This file lists all the commands that were done on the computer and what happened when they ran.
- Finally, it opens the "server-report.html" file on the user's computer using Firefox.
