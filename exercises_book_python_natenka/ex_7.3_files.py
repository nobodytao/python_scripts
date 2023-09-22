#!/usr/bin/env python3

from sys import argv

mac_file='CAM_table.txt'

resultlist=[]

with open(mac_file,'r') as macfile:
    for strfile in macfile:
        listofcolumns = strfile.split()
        if (listofcolumns) and (len(listofcolumns) == 4) and (listofcolumns[1][0].isdigit()):
            listofcolumns.remove('DYNAMIC')
            listofcolumns[0]=int(listofcolumns[0])
            resultlist.append(listofcolumns)
    
    resultlist = sorted(resultlist)

    for itemlist in resultlist:
        itemlist[0]=str(itemlist[0])
        print("{:7}{:17}{:10}".format(itemlist[0],itemlist[1],itemlist[2]))
