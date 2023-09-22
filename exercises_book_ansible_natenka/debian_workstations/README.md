debian_workstations
=========

Role created to get information from virtual machines running Debian 12 operating systems.

The 'all_roles.yml' playbook checks computers running Debian 12 by executing tasks with a list of commands such as 'whoami,' 'ip a,' and 'free -m' in the terminal. These commands are stored in 'vars/main.yml,' and the results are displayed on the screen using the 'Output var to the screen' handler from 'handlers/main.yml'.
