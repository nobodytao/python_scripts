from jinja2 import Environment, FileSystemLoader
import yaml, sys, os, ex_20_jinja

'''MAIN'''
if __name__ == "__main__":
    data_file = "data_files/router_info.yml"
    template_file = "templates/cisco_router_base.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(ex_20_jinja.generate_config(template_file, data))