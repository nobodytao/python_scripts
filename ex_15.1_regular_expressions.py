import re

def get_ip_from_cfg(filename):
    result_list = []
    with open(filename,'r') as file_settings:
        for one_line in file_settings:
            match = re.search(r'(\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)', one_line)
            if (match):
                result_list.append((match.group(1),match.group(2)))
                print((match.group(1),match.group(2)))

    return result_list

print(get_ip_from_cfg('config_r1.txt'))
