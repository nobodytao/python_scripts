import locale, re, csv, yaml, draw_network_graph, pprint

def generate_topology_from_cdp(list_files, save_filename):
    '''
    Reads connections between devices 
    from files with output from command show cdp neighbors
    '''
    with open(save_filename, 'w') as save_file:
        result_dict = {}
        for one_file in list_files:
            device_dict_port = {}
            with open(one_file, 'r') as settings_file:
                device_name = ''
                for one_line in settings_file:
                    device_dict = {}
                    match_device = re.search(r'(^[A-Za-z0-9]+)>', one_line)
                    if match_device:
                        device_name = match_device.group(1)
                    match_settings = re.search(r'([A-Za-z0-9]+) +(\S+ \d+/\d+) +\S+ +R? +S? +I?+ +[A-Za-z0-9-]+ +(\S+ \d+/\d+)', one_line)
                    if match_settings:
                        device_dict[match_settings.group(1)] = match_settings.group(3)
                        device_dict_port[match_settings.group(2)] = device_dict         
            result_dict[device_name] = device_dict_port
        yaml.dump(result_dict, save_file)
    return result_dict


def transform_topology(yaml_file):
    '''
    Makes a dictionary from the yaml-file 
    with connections between devices
    '''
    topology_from_file = {}
    with open(yaml_file, 'r') as save_file:
        result_dict = dict()
        result_list = []
        topology_from_file = yaml.safe_load(save_file)
        for key_dict in topology_from_file:
            inner_1lvl_dict = topology_from_file[key_dict]
            for key_inner_dict in inner_1lvl_dict:
                inner_2lvl_dict = inner_1lvl_dict[key_inner_dict] 
                for key_2lvl_inner_dict, value in inner_2lvl_dict.items():
                    tuple2lvl = (key_2lvl_inner_dict, value)
                    tuple1lvl = (key_dict, key_inner_dict)
                    result_list.append(sorted((tuple2lvl, tuple1lvl)))
        result_list = (sorted(result_list))
        for item_list in result_list:
            result_dict[item_list[0]] = item_list[1]

    return result_dict

'''
MAIN
'''
list_of_files = ['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_r4.txt', 'sh_cdp_n_r5.txt', 'sh_cdp_n_r6.txt']
save_to_filename = 'sh_cdp_neighbor.yaml'

generate_topology_from_cdp(list_of_files, save_to_filename)

dict_for_draw = transform_topology(save_to_filename)

draw_network_graph.draw_topology(dict_for_draw)