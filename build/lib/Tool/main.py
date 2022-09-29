import json
import os
from Tool.cfg_to_dict import cfg_to_dict
from collections.abc import MutableMapping
import yaml
from yaml.loader import FullLoader
from Tool.conf_to_dict import conf_to_dict
from Tool.yaml_to_dict import yaml_to_dict

import configparser
config = configparser.ConfigParser()






# Method to convert the yaml file to a dictionary
def yaml_to_dict(filename):
    with open(filename, 'r') as stream:
        dict=yaml.load(stream, Loader=FullLoader)
        return dict

#Method to convert the .cfg file to a dictionary
def cfg_to_dict(filename):
    config.read(filename)
    dict = {}
    for section in config.sections():
        dict[section] = {}
        for option in config.options(section):
            dict[section][option] = config.get(section, option)
    return dict

# Program to convert .conf file to dict
def conf_to_dict(filename):
    config.read(filename)

    dict = {}
    for section in config.sections():
        dict[section] = {}
        for option in config.options(section):
            dict[section][option] = config.get(section, option)

    return dict


#Method to make a nested dictionary flat
def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


#Main function to handle control flow
def control_flow(path):
    """Control flow of the program."""
    path = path.strip()
    if os.path.exists(path):
        extension= path.split(".")[-1]
        if extension == "conf":
            output =conf_to_dict(path)
        elif extension == "yaml":
            output = yaml_to_dict(path)
        elif extension == "cfg":
            output = cfg_to_dict(path)
    
    output = flatten_dict(output)
    # print(output)

    output_format = input("Enter the output format, choose 'json' or 'env': ").strip()
    if output_format == "json":
        json_object = json.dumps(output, indent = 4) 
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    elif output_format == "env":
        with open("output.env", "w") as f:
            for key, val in output.items():
                f.write(f"{key}={val}\n")

control_flow("D:\Test_Sacumen\Sacumen\sample.yaml")
        


