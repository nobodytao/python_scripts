import ipaddress, subprocess
from tabulate import tabulate

def ping_ip_addresses(list_ranges):
    '''
    This function determines whether the IP is alive or unreachable
    '''

    def convert_ranges_to_ip_list(list_ranges):
        '''
        This function converts a list of ranges into a list of IPs
        '''
        list_of_ips = []
        for one_list in list_ranges:
            position = one_list.find("-")
            start_of_range = None
            end_of_range = None
            if (position > 0):
                splitted_range = one_list.split('-')
                start_of_range = splitted_range[0].split('.')
                end_of_range = splitted_range[1].split('.')
                for addr in range(int(start_of_range[len(start_of_range)-1]),int(end_of_range[len(end_of_range)-1])+1):
                    list_of_ips.append("{}.{}.{}.{}".format(start_of_range[0],start_of_range[1],start_of_range[2],addr) )
            else:
                list_of_ips.append(one_list)
        return list_of_ips

    '''
    Function ping_ip_addresses continues
    '''
    list_ips = convert_ranges_to_ip_list(list_ranges)

    list_alive=[]
    list_unreach=[]
    for ip_addr in list_ips:
        reply = subprocess.run(['ping', '-c', '1','-n', ip_addr])

        if reply.returncode == 0:
            list_alive.append(ip_addr)
        else:
            list_unreach.append(ip_addr)
    return list_alive, list_unreach

def print_ip_table(list_ranges):
    '''
    This function only prints the result table of alive and unreachable IPs
    '''
    result_table = ping_ip_addresses(list_ranges)

    dict_for_print = {}

    dict_for_print = {'Reachable': result_table[0],'Unreachable': result_table[1]}

    print(tabulate(dict_for_print, headers="keys"))
    return result_table

'''
MAIN
'''
list_of_ranges = ['127.0.0.1','10.99.0.1-2','127.0.0.1-127.0.0.15','77.224.56.34-77.224.56.37','5.255.255.242-250']

print()
print_ip_table(list_of_ranges)