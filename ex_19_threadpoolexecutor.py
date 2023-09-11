import subprocess
from itertools import repeat
from concurrent.futures import ThreadPoolExecutor

def pinging(ip, command):
    print('Pinging: ', ip )
    res = subprocess.run(command + ip, shell=True, stdout=subprocess.PIPE)
    data_to_file = res.stdout.decode('utf-8')

    with open('/home/nobodytao/github_repos/python_scripts/ping_files/'+ip+'.txt', 'a+') as file_to_write:
        file_to_write.write(data_to_file)

def ping_ip_addresses(ip_list, limit):
    with ThreadPoolExecutor(max_workers = limit) as executor:
        result = executor.map(pinging, ip_list, repeat('ping -c 5 '))


listip = ['192.168.178.1', '192.168.178.2', '127.0.0.2', '192.168.178.3', '8.8.8.8', '127.0.0.1', '192.168.178.4', '192.168.178.5', 'www.ya.ru', 'vc.ru', 'github.com']
limit_workers = 2
ping_ip_addresses(listip, limit_workers)