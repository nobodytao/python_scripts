#[«add», «10», «20»] - switchport trunk allowed vlan add 10,20
#[«del», «17»] - switchport trunk allowed vlan remove 17
#[«only», «11», «30»] - switchport trunk allowed vlan 11,30


trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

trunk = {"0/1": ["add", "10", "20", "2"], "0/2": ["only", "11", "30", "55", "80"], "0/4": ["del", "17"], "0/5": ["del"]}

for intf, command_and_port in trunk.items():
    additional_command=''
    ports=''
    print ("interface FastEthernet " + intf)
    if command_and_port[0] == 'add':
        additional_command = 'add'
        command_and_port.remove('add')
    elif command_and_port[0] == 'del':
        additional_command = 'remove'
        command_and_port.remove('del')
    else:
        additional_command = 'allowed'
        command_and_port.remove('only')
    for count_command in range(2):
        print(" ", trunk_template[count_command])

    ports = ",".join(command_and_port)
    
    print (" ", trunk_template[2], additional_command, ports)
