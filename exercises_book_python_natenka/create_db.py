#!/usr/bin/env python3

import sqlite3, os

def creating_or_not_tables(dbfilename):
    '''
    Creating new database named 'exercisebase.db'
    '''
    connection = sqlite3.connect(dbfilename)   
    data_for_new_table = '''create table switches (
                            hostname    text not null primary key,
                            location    text
                            );

                            create table dhcp (
                            mac          text primary key,
                            ip           text,
                            vlan         text,
                            interface    text,
                            switch       text not null references switches(hostname)
                            );'''
    
    cursor = connection.cursor()
    cursor.executescript(data_for_new_table)

'''
MAIN
'''
if __name__ == "__main__":

    db_filename = 'exercisebase.db'

    db_exists = os.path.exists(db_filename)

    if db_exists:
        print('Database already existed')
    else:
        print('New database and table "dhcp" created')

    creating_or_not_tables(db_filename)
