import subprocess, os, ipaddress

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

