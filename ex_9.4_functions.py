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
        NextCommand = ''
        list2lvlcommands = ['0']
        while not(fileline.startswith('end')):
            fileline = config_file.readline().strip("\n")
            if not(fileline.startswith('!')):
                if not(ignore_command(fileline, ignore)):
                     
                    if not(fileline.startswith(" ")):
                       if (len(list2lvlcommands) == 0):
                          resultdict[NextCommand]=list2lvlcommands    
                       list2lvlcommands = []
                       NextCommand = fileline
                       
                    if (fileline.startswith(" ")):
                        while fileline.startswith(" "):
                            if not(ignore_command(fileline, ignore)):
                                list2lvlcommands.append(fileline.strip())
                            fileline = config_file.readline().strip("\n")
                        resultdict[NextCommand]=list2lvlcommands
                    
    return resultdict

print(convert_config_to_dict('config_sw1.txt'))
