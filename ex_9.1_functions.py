#!/usr/bin/env python3

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

dict_arg={'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}

dict_arg2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def accesslist(dictionary_with_interfaces,template_for_dictionary,template_for_port=None):
    access_list = []
    for dict_key in dictionary_with_interfaces.keys():
        access_list.append("interface "+dict_key)
        for acc_item in template_for_dictionary:
            if acc_item.startswith('switchport access vlan'):
                access_list.append(acc_item+" "+str(dictionary_with_interfaces[dict_key]))
            else: 
                access_list.append(acc_item)
        if  template_for_port:
            for port_item in template_for_port:
                access_list.append(port_item)
            
    return access_list

print(accesslist(dict_arg2,access_mode_template))
print("")
print(accesslist(dict_arg2,access_mode_template,port_security_template))