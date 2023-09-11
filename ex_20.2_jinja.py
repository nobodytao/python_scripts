from jinja2 import Environment, FileSystemLoader
import yaml, sys, os

def generate_config(templatefile, data_from_yml):
    env = Environment(loader = FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
    templ = env.get_template(templatefile)
    result = templ.render(data_from_yml)

    return result

'''MAIN'''
if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))