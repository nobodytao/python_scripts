#!/usr/bin/env python3

argvvlan = input('Input number of vlan: ')

mac_file='CAM_table.txt'

resultlist=[]

with open(mac_file,'r') as macfile:
    for strfile in macfile:
        listofcolumns = strfile.split()
        if (listofcolumns) and (len(listofcolumns) == 4) and (listofcolumns[1][0].isdigit()):
            if listofcolumns[0] == argvvlan:
                listofcolumns.remove('DYNAMIC')
                print("{:7}{:17}{:10}".format(listofcolumns[0],listofcolumns[1],listofcolumns[2]))