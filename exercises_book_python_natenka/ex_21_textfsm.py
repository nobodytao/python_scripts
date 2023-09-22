import textfsm, tabulate

def parse_command_output(template, str_to_output):
    print(str_to_output)
    with open(template) as file_with_template:
        fsm = textfsm.TextFSM(file_with_template)
        result = fsm.ParseText(str_to_output)
        header = fsm.header
        print(header)
        print(result)



'''MAIN'''
if __name__ == "__main__":
    with open('sh_ip_int_br.txt', 'r') as f:
        output = f.read()

    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)