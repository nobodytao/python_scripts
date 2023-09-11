from jinja2 import Environment, FileSystemLoader
import yaml


env = Environment(loader=FileSystemLoader("."))
templ = env.get_template("cfg_template.txt")

liverpool = {"id": "11", "name": "Liverpool", "int": "Gi1/0/17", "ip": "10.1.1.10"}
print(templ.render(liverpool))