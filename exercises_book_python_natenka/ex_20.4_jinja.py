from jinja2 import Environment, FileSystemLoader
import yaml, sys, os, ex_20_jinja

'''MAIN'''
if __name__ == "__main__":
    data_file = "data_files/add_vlan_to_switch.yaml"
    template_file = "templates/add_vlan_to_switch.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(ex_20_jinja.generate_config(template_file, data))