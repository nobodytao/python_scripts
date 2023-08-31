import graphviz

def parse_cdp_neighbors(command_output_files): 
    '''
    The function should return a dictionary like this:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
    ("R4", "Fa0/2"): ("R6", "Fa0/0")}
    '''   
    result_dict = {}

    for file_command in command_output_files:
        with open(file_command) as f:
            strings = f.read().split('\n')
        
            tuple_key = ()
            tuple_val = ()

            for position, onestr in enumerate(strings):
                if (">") in onestr:
                    dict_key_name = onestr.split('>')[0] 
                if ("Device ID") in onestr:
                    break
                        
            for item_list in range(position+1): strings.pop(0)

            for onestr in strings:
                if len(onestr) > 0:
                    split_str = onestr.split()
                    tuple_key = (dict_key_name,'Fa'+split_str[2])
                    tuple_val = (split_str[0],'Fa'+split_str[len(split_str)-1])
                    
                    result_dict[tuple_key] = tuple_val     

    return (result_dict)    
    

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
    ]      
        
if __name__ == "__main__":
     print(parse_cdp_neighbors(infiles))