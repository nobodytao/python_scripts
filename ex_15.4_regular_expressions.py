import re

def get_ints_without_description(file_name):
    with open('config_r1.txt','r') as file_settings:
        is_interfase = True
        is_description = True
        interface = ''
        list_of_interfaces = []
        match_interface = ''

        for one_line in file_settings:
            match_interface = re.search(r'^interface \S+', one_line)
            if match_interface:
                is_interfase = True
                interface = match_interface.group()

            if re.search(r'!', one_line):
                if (is_interfase) and not(is_description):
                    list_of_interfaces.append(interface) 
                is_interfase = False
                is_description = False

            if (re.search(r' description ', one_line)):
                is_description = True

    return list_of_interfaces

print(get_ints_without_description('config_r1.txt'))