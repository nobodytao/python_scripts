import ipaddress, subprocess

def convert_ranges_to_ip_list(list_ranges):
    '''
    This function converts a list of ranges into a list of IPs
    '''
    pass

def ping_ip_addresses(list_ips):
    '''
    This function determines whether the IP is alive or unreachable
    '''
    list_alive=[]
    list_unreach=[]
    for ip_addr in list_ips:
        reply = subprocess.run(['ping', '-c', '3','-n', ip_addr])

        if reply.returncode == 0:
            list_alive.append(ip_addr)
        else:
            list_unreach.append(ip_addr)
    return list_alive, list_unreach

list_of_ranges = ['127.0.0.1','10.10.0.1','10.10.2.4','127.0.0.1','192.168.212.3']

#print(ping_ip_addresses(list_of_ranges)
convert_ranges_to_ip_list(list_of_ranges)