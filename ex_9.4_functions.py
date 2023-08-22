ignore = ["duplex", "alias", "Current configuration"]

def ignore_command(command, ignore):
    """
    The function checks if the command contains a word from the ignore list.

     command - a string. Team to check
     ignore - list. Word list

     returns
     * True if the command contains a word from the ignore list
     * False - if not   
     """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

resultdict={}

def convert_config_to_dict(filename):
    with open(filename,'r') as config_file:
        
        fileline = ''
        list2lvlcommands = []
        resultlist=[]

        while not(fileline.startswith('end')):
            fileline = config_file.readline().strip("\n")
            if not(fileline.startswith('!')) and (not(ignore_command(fileline, ignore))):

                if (fileline.startswith(" ")):
                    list2lvlcommands.append(fileline.strip(" "))
                    
                else:
                    resultlist.append(list2lvlcommands)
                    list2lvlcommands = []
                    resultlist.append(fileline)
 
    resultlist.pop(len(resultlist)-1)
    resultlist.pop(0)

    for listindex in range (0,int(len(resultlist)),2):
        resultdict[resultlist[listindex]]=resultlist[listindex+1]

    return (resultdict)               
               
print(convert_config_to_dict('config_sw1.txt'))
