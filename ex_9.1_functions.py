#!/usr/bin/env python3

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

dict_arg={'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}

def accesslist(dictionary_with_interfaces):
    access_list = []
    return access_list

print(accesslist(dict_arg))