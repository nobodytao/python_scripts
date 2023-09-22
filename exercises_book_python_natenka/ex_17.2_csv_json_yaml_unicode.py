import locale, re, csv


def parse_sh_version(sh_version_str):
    '''
    ios - «12.4(5)T»
    image - «flash:c2800-advipservicesk9-mz.124-5.T.bin»
    uptime - «5 days, 3 hours, 3 minutes»
    return tuple with 3 elements
    '''
    result_tuple = ()
    match = re.search(r'Cisco IOS [A-Z a-z()0-9,-]+, Version (\S+), [A-Z a-z()0-9,-/:_\[\]]+ router uptime is ([A-Z a-z0-9,]+), System returned to ROM[A-Z a-z()0-9,-/:_\[\]]+System image file is \"([A-Z a-z()0-9,-/:_\[\]]+)\"', sh_version_str)                      
    if match: 
        result_tuple = match.groups()
    
    return result_tuple


def write_inventory_to_csv(file_names, file_output):
    with open(file_output,'w') as file_out:
        for single_file in file_names:
            tuple_to_output = ()
            with open(single_file,'r') as filename:
                one_str = filename.readlines()
                one_str = str([string_from_list.strip('\n') for string_from_list in one_str]).strip('[]').replace('\'','')
                str.encode(one_str, encoding = 'UTF-8')
                tuple_to_output = parse_sh_version(one_str)
                write_to_file = csv.writer(file_out)
                write_to_file.writerow(tuple_to_output)
        
'''
MAIN
'''
file_names_list=['sh_version_r1.txt','sh_version_r2.txt','sh_version_r3.txt']
file_to_output = 'sh_version.csv'
write_inventory_to_csv(file_names_list, file_to_output)