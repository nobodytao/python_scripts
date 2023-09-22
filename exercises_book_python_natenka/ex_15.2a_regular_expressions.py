import re

headers = ["hostname", "ios", "platform"]

data = [
    ("R1", "12.4(24)T1", "Cisco 3825"),
    ("R2", "15.2(2)T1", "Cisco 2911"),
    ("SW1", "12.2(55)SE9", "Cisco WS-C2960-8TC-L"),
]

def convert_to_dict(headers_list, data_list):
    str_head = ''
    for name_p in headers_list:
        str_head = str_head + r'\''+'(?P<'+name_p+'>'+r'(\w*\s*\d*.*\(*\)*))\', '
        
    str_head = str_head[:-2]

    for data_line in data_list:
        str_data = str(data_line)
        match = re.search(str_head, str_data)
        print(match.groupdict())
        

convert_to_dict(headers, data)