#First dictionary 'Access' have to be like this:
#{"FastEthernet0/12": 10,
# "FastEthernet0/14": 11,
# "FastEthernet0/16": 17}

#Second dictionary 'Trunk' have to be like this:
#{"FastEthernet0/1": [10, 20],
# "FastEthernet0/2": [11, 30],
# "FastEthernet0/4": [17]}


def get_int_vlan_map(file_name):
    with open('config_sw1.txt','r') as config_file:
        for fileline in config_file:
            print(fileline.strip())
        
get_int_vlan_map('config_sw1.txt')