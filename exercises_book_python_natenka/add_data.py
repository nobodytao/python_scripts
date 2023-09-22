#!/usr/bin/env python3

import sqlite3, os, create_db, textfsm, re

def update_table_dhcp(filewithdata, templatefromfile, dbname):
    '''
    Updating table dhcp with new data fron file 'sw1_dhcp_new_info.txt'
    '''
    conn = sqlite3.connect(dbname)  
    cur = conn.cursor()
    result = []
    with open(templatefromfile, 'r') as templ:
        template_dhcp = textfsm.TextFSM(templ)
    with open(filewithdata, 'r') as dhcp:
            device_name = re.search(r'(\S+)_dhcp', dhcp.name).group(1)
            print("From file", dhcp.name)
            data_dhcp = dhcp.read()
            result = template_dhcp.ParseText(data_dhcp)
            for one_dhcp_device in result:
                one_dhcp_device = tuple(one_dhcp_device) + (device_name,) + (True,)
                print("adding row:", one_dhcp_device, "INTO table 'dhcp'")
                try:
                    query = "REPLACE into dhcp values (?,?,?,?,?,?)"
                    cur.execute(query, one_dhcp_device)
                    conn.commit()
                except sqlite3.IntegrityError as err:
                    print('Something wrong: ', err)
            result.clear()


def filling_tables(switchfile, dhcpfiles, dbname):
    '''
    Filling new tables 'dhcp' and 'switches' from files:
    'sw1_dhcp_snooping.txt', 
    'sw2_dhcp_snooping.txt', 
    'sw3_dhcp_snooping.txt',
    switches.yml
    '''
    conn = sqlite3.connect(dbname)  
    cur = conn.cursor()
    result = []
    with open('dhcp_template.fsm', 'r') as templ:
        template_dhcp = textfsm.TextFSM(templ)
    for dhcpfile in dhcpfiles:
        with open(dhcpfile, 'r') as dhcp:
            device_name = re.search(r'(\S+)_dhcp', dhcp.name).group(1)
            print("From file", dhcp.name)
            data_dhcp = dhcp.read()
            result = template_dhcp.ParseText(data_dhcp)
            for one_dhcp_device in result:
                one_dhcp_device = tuple(one_dhcp_device) + (device_name,)
                print("adding row:", one_dhcp_device, "INTO table 'dhcp'")
                try:
                    query = "INSERT into dhcp values (?,?,?,?,?)"
                    cur.execute(query, one_dhcp_device)
                    conn.commit()
                except sqlite3.IntegrityError as err:
                    print('Something wrong: ', err)
            result.clear()

    with open('sw_template.fsm', 'r') as templ:
        template_sw = textfsm.TextFSM(templ)
        with open(switchfile, 'r') as sw:
            data_sw = sw.read()
            result = template_sw.ParseText(data_sw)
            print("From file", sw.name)
            for one_sw_device in result:
                one_sw_device = tuple(one_sw_device)
                print("adding row:", one_sw_device, "INTO table 'switches'")
                try:
                    query = "INSERT into switches values (?,?)"
                    cur.execute(query, one_sw_device)
                    conn.commit()
                except sqlite3.IntegrityError as err:
                    print('Something wrong: ', err)
            result.clear()
'''
MAIN
'''

swith_file = 'switches.yml'
dhcp_files = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']

if __name__ == "__main__":

    db_filename = 'exercisebase.db'

    db_exists = os.path.exists(db_filename)

    if db_exists:
        print('Database already existed. Your tables will be filled with data')
        filling_tables(swith_file, dhcp_files, db_filename)
    else:
        print('Database not existed. You need to create database')
        permission = input('Do you want to create a database (y/n): ')
        if permission == 'y':
            create_db.creating_or_not_tables(db_filename)
            print('Database and tables created')    
            permission = input('Do you want to fill in the tables (y/n): ')
            if permission == 'y':
                filling_tables(swith_file, dhcp_files, db_filename)