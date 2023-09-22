from jinja2 import Environment, FileSystemLoader
import yaml, sys, os, ex_20_jinja

def  create_vpn_config(templatefiles, data):
    result = ''
    for templfile in templatefiles:
        env = Environment(loader = FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
        templ = env.get_template(templfile)
        #print(data)
        result += templ.render(data) + "\n\n" + "*" * 10 + "\n\n"

    return result


'''MAIN'''
if __name__ == "__main__":
    
    data_dict = {
    'tun_num': 10,
    'wan_ip_1': '192.168.100.1',
    'wan_ip_2': '192.168.100.2',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
    }
    
    template_files = ['templates/gre_ipsec_vpn_1.txt','templates/gre_ipsec_vpn_2.txt']
    print(create_vpn_config(template_files, data_dict))