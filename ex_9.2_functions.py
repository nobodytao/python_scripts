trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(intf_vlan_mapping,trunk_template):
    resultdict={}
    for intf_vlan in intf_vlan_mapping:
        resultlist=[]
        for item_template in trunk_template:
            if item_template.startswith('switchport trunk allowed vlan'):
                resultlist.append(item_template + " " + str(intf_vlan_mapping[intf_vlan]).strip("[]"))
            else:
                resultlist.append(item_template)
        resultdict[intf_vlan] = resultlist
    return resultdict

print(generate_trunk_config(trunk_config,trunk_mode_template))