import ipaddress, subprocess

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

def ping_ip_addresses(list_ranges):
    '''
    This function determines whether the IP is alive or unreachable
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

list_of_ranges = ['127.0.0.1','77.88.55.242-77.88.55.252','127.0.0.1-127.0.0.15','10.10.212.3','10.10.0.1','77.88.55.230-2']

print(ping_ip_addresses(list_of_ranges))