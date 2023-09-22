import re

def parse_sh_ip_int_br(filename):
    interface = ''
    ipaddress = ''
    interf_status = ''
    interf_protocol = ''
    result_list = []
    with open(filename,'r') as file_with_commands:
        for one_line in file_with_commands:
            if (re.search(r'\S+\d/*\d* ', one_line)):
                match = re.search(r'(\S+\d/*\d*/*\d*) +((\d+\.\d+\.\d+\.\d+)|(unassigned))( +\S+){2} +(\S+ ?\S*) +(\S+)', one_line)

                interface = match.group(1)
                ipaddress = match.group(2)
                interf_status = match.group(6)
                interf_protocol = match.group(7)

                result_list.append((interface, ipaddress, interf_status, interf_protocol))

    return result_list



print(parse_sh_ip_int_br('sh_ip_int_br.txt'))