#!/usr/bin/env python3

from sys import argv

old_file = argv[1]
new_file = argv[2]

ignore = ["duplex", "alias", "configuration"]
resultstr=''

with open(old_file,'r') as swfile, open(new_file,'w') as newfile:
    for strfile in swfile:
        contain_ignore=False
        for ignoreitem in ignore:
            if ignoreitem in strfile:
                contain_ignore=True
        if not(strfile.startswith('!')) and (contain_ignore==False):
            resultstr+=strfile
    newfile.write(resultstr)
        

