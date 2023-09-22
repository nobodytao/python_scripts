import re

def generate_description_from_cdp(file_name):
    result_dict = {}
    with open(file_name,'r') as connection_file:
        for one_line in connection_file:
            match = re.search(r'^(\S+) +(\S+ \d+/\d+) +\d+ +R? ?S? ?I? +\S+ +(\S+ \d+/\d+)', one_line)
            if match:
                result_dict[match.group(2)] = "description Connected to " + match.group(1) + " port " + match.group(3)

    return result_dict

print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))