import locale, re, csv

def write_dhcp_snooping_to_csv(list_of_filenames, file_output):
    with open(file_output,'w') as file_out:
        data_to_write = ''
        for filename in list_of_filenames: 
            name_of_device = ''
            with open(filename,'r') as file_with_command:
                name_of_device = re.match(r'^\S+?_',file_with_command.name)
                name_of_device = name_of_device.group().strip('_')
                for one_line in file_with_command:
                    match = re.search(r'((([A-F0-9]+:)+[A-F0-9]+) +(\d+\.\d+\.\d+\.\d+)+ +\S+ +\S+ +(\d+) +(\S+\d+/?\d?))', one_line)
                    if match:
                        writer = csv.writer(file_out)
                        data_to_write = [name_of_device,match.group(2),match.group(4),match.group(5),match.group(6)]
                        writer.writerow(data_to_write)



filenames_list = ['sw1_dhcp_snooping.txt','sw2_dhcp_snooping.txt','sw3_dhcp_snooping.txt']
file_for_output = 'dhcp_snooping.csv'

write_dhcp_snooping_to_csv(filenames_list, file_for_output)