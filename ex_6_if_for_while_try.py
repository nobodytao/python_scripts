ip = input('Введите IP-адрес в формате 10.10.0.1: ')

#«unicast» - если первый байт в диапазоне 1-223
#«multicast» - если первый байт в диапазоне 224-239
#«local broadcast» - если IP-адрес равен 255.255.255.255
#«unassigned» - если IP-адрес равен 0.0.0.0
#«unused» - во всех остальных случаях

IPlist=ip.split('.')
if int(IPlist[0]) in range(1,223): 
    print(ip,' «unicast»')
elif int(IPlist[0]) in range(224,239):
    print(ip,' «multicast»')
elif ip=='255.255.255.255':
    print(ip,'«local broadcast»')
elif ip=='0.0.0.0':
    print(ip,'«unassigned»')
else:
    print(ip,'«unused»')