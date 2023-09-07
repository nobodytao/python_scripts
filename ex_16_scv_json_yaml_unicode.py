import subprocess, locale, csv, yaml
print("\N{LATIN SMALL LETTER O WITH DIAERESIS}", ord('ö'), chr(246))
b1 = b'\xd0\xb4\xd0\xb0'
bytes2 = b'\x68\x65\x6c\x6c\x6f'
b1 = b1.decode('UTF8')
b3 = str.encode('да', encoding = 'utf-8')
b4 = bytes.decode(b'\xd0\xb4', encoding='utf-8')
print(b1, bytes2, b3, b4)

result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-8')
print(type(result))
print(type(output))

print(locale.getpreferredencoding())
f = open('test_encoding.txt','w')
print(f)


with open('sw_data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('sw_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)


import yaml
from pprint import pprint

with open('info.yaml') as f:
    templates = yaml.safe_load(f)

pprint(templates)