#!/usr/bin/env python3

import sqlite3
from sys import argv

def get_data_from_db(field, data, database_name):
    table_w = 81
    def get_data_from_table(query, table_width):
        '''
        Gets data from 1 table with query from parent def
        '''
        connect = sqlite3.connect(database_name)
        curs = connect.cursor()
        curs.execute(query)
        print("-" * table_width)
        print("{:20}{:19}{:5}{:19}{:8}{:^8}".format('mac','ip','vlan','interface','switch','active'))
        print("-" * table_width)
        for one_row in curs.fetchall():
            print("{:20}{:19}{:5}{:19}{:8}{:^8}".format(one_row[0],one_row[1],one_row[2],one_row[3],one_row[4],one_row[5]))
        print("-" * table_width)    
    

    def get_data_from_table_active_nacive(query, sub_query, table_width):
        print("-" * table_width)
        print("Active devices:")
        print("-" * table_width)
        print (query + ' WHERE active = 1' + sub_query)
        get_data_from_table(query + ' WHERE active = 1' + sub_query, table_width)

        print("-" * table_width)
        print("NOT active devices:")
        print("-" * table_width)
        print (query + ' WHERE active = 0' + sub_query)
        get_data_from_table(query + ' WHERE active = 0' + sub_query, table_width)


    '''
    Prints result table in case of number of argvs
    '''
    if (field == '') and (data == ''):
        print("-" * table_w)
        print("Whole table 'dhcp':")
        print("-" * table_w)
        get_data_from_table_active_nacive('SELECT * from dhcp', '', table_w)
        
    else:
        print("-" * table_w)
        print("Rows from table 'dhcp' matching the entered arguments:")
        print("-" * table_w)
        get_data_from_table_active_nacive('SELECT * from dhcp', ' AND '+field+' = '+data, table_w)


'''
MAIN
'''
dbname = 'exercisebase.db'

if (len(argv) == 1):
    get_data_from_db('','', dbname)
elif (len(argv) == 3):
    get_data_from_db(argv[1], argv[2], dbname)
else:
    print('You need to input 0 or 2 arguments.')
    print("0 args: Whole table 'dhcp'.")
    print("2 args: Rows from table 'dhcp' with field [argv 1] and data in this field [argv 2]")
    print('Fields: mac | ip | vlan | interface | switch')
