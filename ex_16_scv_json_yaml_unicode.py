import subprocess 
#print("\N{LATIN SMALL LETTER O WITH DIAERESIS}", ord('ö'), chr(246))
#b1 = b'\xd0\xb4\xd0\xb0'
#bytes2 = b'\x68\x65\x6c\x6c\x6f'
#b1 = b1.decode('UTF8')
#b3 = str.encode('да', encoding = 'utf-8')
#b4 = bytes.decode(b'\xd0\xb4', encoding='utf-8')
#print(b1, bytes2, b3, b4)

result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'], stdout=subprocess.PIPE)

print(result)
