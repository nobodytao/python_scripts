import re

def get_ip_from_cfg(filename):
    result_dict = {}
    list_ips = []
    is_interface = True

    with open(filename,'r') as file_settings:
        for one_line in file_settings:

            if (re.search(r'interface [a-zA-Z]+\S+\n', one_line)):
                interface = re.search(r'(interface [a-zA-Z]+\S+)\n', one_line).group(1)
                is_interface = True

            if (re.search(r'!\n', one_line)):
                is_interface = False
                list_ips = []

            match = re.search(r'(\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)', one_line)
            if (match) and (is_interface == True):
                #is_interface = False
                list_ips.append((match.group(1),match.group(2)))
                result_dict[interface] = list_ips

    return result_dict

print(get_ip_from_cfg('config_r2.txt'))
