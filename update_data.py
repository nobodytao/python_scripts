import sqlite3, os, textfsm, re, add_data

add_data.update_table_dhcp('sw1_dhcp_new_info.txt', 'dhcp_template.fsm', 'exercisebase.db')