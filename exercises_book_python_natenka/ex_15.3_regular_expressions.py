import re

def convert_ios_nat_to_asa(file_nat, file_asa):
    result_str_to_file = ''
    with open(file_nat,'r') as nat_file:
        for one_line in nat_file:
            one_line = one_line.strip('\n')
            match = re.search(r' (\d+\.\d+\.\d+\.\d+) (\d+) \w+ \S+ (\d+)', one_line)
            result_str_to_file = result_str_to_file + 'object network LOCAL_{0}\n host {0}\n nat (inside,outside) static interface service tcp {1} {2}\n'.format(match.group(1),match.group(2),match.group(3))
    
    result_str_to_file = result_str_to_file[:-1]
    
    with open(file_asa, 'w') as asa_file:
        asa_file.write(result_str_to_file)

convert_ios_nat_to_asa('cisco_nat_config.txt','cisco_nat_to_asa.txt')