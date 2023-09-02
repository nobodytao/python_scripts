import subprocess, os, ipaddress
from tabulate import tabulate

#standard input/output stream
result = subprocess.run(['ls', '-ls'], stdout=subprocess.PIPE)
print(result.stdout.decode('utf-8'))

#Turn off standard input/output stream, only result
result = subprocess.run(['ls', '-ls'], stdout=subprocess.DEVNULL)
print(result.stdout)
print(result.returncode)

#Stderr
result = subprocess.run(['ping', '-c', '3', '-n', 'a'], stderr=subprocess.PIPE, encoding='utf-8')
print(result.stderr)

print(os.path.abspath("python_scripts"))

ipv4 = ipaddress.ip_address('10.0.1.1')
print(ipv4)

subnet1 = ipaddress.ip_network('80.0.1.0/28')
print(subnet1.broadcast_address, subnet1.network_address, subnet1.netmask, subnet1.num_addresses, subnet1.prefixlen)
print(list(subnet1.hosts()))

for ip in subnet1:
    print(ip)

IP1 = '10.0.1.1/24'
IP2 = '10.0.1.0/24'

def check_if_ip_is_network(ip_address):
        try:
            ipaddress.ip_network(ip_address)
            return True
        except ValueError:
            return False

print(check_if_ip_is_network(IP1))

#Tabulate module
sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
     ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
     ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
     ('Loopback0', '10.1.1.1', 'up', 'up'),
     ('Loopback100', '100.0.0.1', 'up', 'up')]

columns = ['Interface', 'IP', 'Status', 'Protocol']

print(tabulate(sh_ip_int_br, headers=columns))

list_of_dicts=[{'IP': '15.0.15.1',
  'Interface': 'FastEthernet0/0',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.0.12.1',
  'Interface': 'FastEthernet0/1',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.0.13.1',
  'Interface': 'FastEthernet0/2',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '10.1.1.1',
  'Interface': 'Loopback0',
  'Protocol': 'up',
  'Status': 'up'},
 {'IP': '100.0.0.1',
  'Interface': 'Loopback100',
  'Protocol': 'up',
  'Status': 'up'}]

print(tabulate(list_of_dicts, headers='keys'))
print(tabulate(list_of_dicts, headers='keys', tablefmt="grid"))

with open('table_of_IPs.html','w') as html_file:
     html_file.writelines(tabulate(list_of_dicts, headers='keys', tablefmt='html'))

print(tabulate(list_of_dicts, headers='keys', tablefmt='pipe', stralign='center'))
