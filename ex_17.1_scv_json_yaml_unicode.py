import locale, re

def write_dhcp_snooping_to_csv(filenames):
    for filename in filenames:
        with open(filename,'r') as file_with_command:
            print(locale.getpreferredencoding(file_with_command))


filenames_list = ['sw1_dhcp_snooping.txt']

write_dhcp_snooping_to_csv(filenames_list)