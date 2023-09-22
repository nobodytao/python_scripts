import graphviz, draw_network_graph

def parse_cdp_neighbors(command_output_files): 
    '''
    The function should return a dictionary like this:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
    ("R4", "Fa0/2"): ("R6", "Fa0/0")}
    '''   
    result_dict = {}
    set_of_relations=set()

    tuple_key1 = ()
    tuple_val1 = ()
    tuple_key2 = ()
    tuple_val2 = ()


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
                    if dict_key_name.startswith('SW'):
                        tuple_key = (dict_key_name,'Eth'+split_str[2])
                        tuple_val = (split_str[0],'Eth'+split_str[len(split_str)-1])
                    else:
                        tuple_val = (dict_key_name,'Eth'+split_str[2])
                        tuple_key = (split_str[0],'Eth'+split_str[len(split_str)-1])

                    set_of_relations.add(str(tuple_key) + ': ' + str(tuple_val))   
    
    for pair in set_of_relations:
        tuple_key1 = pair.split(': ')[0].split(', ')[0].strip('(\'\'')
        tuple_key2 = pair.split(': ')[0].split(', ')[1].strip('\'\')')
        tuple_key=(tuple_key1,tuple_key2)
        tuple_val1 = pair.split(': ')[1].split(', ')[0].strip('(\'\'')
        tuple_val2 =  pair.split(': ')[1].split(', ')[1].strip('\'\')')
        tuple_val = (tuple_val1,tuple_val2)
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
     draw_network_graph.draw_topology(parse_cdp_neighbors(infiles), output_filename="topology")