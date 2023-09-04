import ipaddress, subprocess

def ping_ip_addresses(list_ips):
    for ip_addr in list_ips:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_addr])

        if reply.returncode == 0:
            print(ip_addr, 'Alive')
        else:
         print(ip_addr, 'Unreachable')

list_of_ips = ['127.0.0.1','10.10.0.1','10.10.2.4','127.0.0.1','192.168.212.3']

ping_ip_addresses(list_of_ips)