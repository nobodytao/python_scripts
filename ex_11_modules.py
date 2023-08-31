def parse_cdp_neighbors(command_output): 
    '''
    The function should return a dictionary like this:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
    ("R4", "Fa0/2"): ("R6", "Fa0/0")}
    '''   

    result_dict = {}
    tuple_key = ()
    tuple_val = ()

    strings = command_output.split('\n')
    for onestr in strings:
        if (">") in onestr:
             dict_key_name = onestr.split('>')[0] 
             break
        
    for position, onestr in enumerate(strings):
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
    
        
        
if __name__ == "__main__":
        with open("sh_cdp_n_sw1.txt") as f:
            print(parse_cdp_neighbors(f.read()))

