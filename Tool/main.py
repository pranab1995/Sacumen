import json
import os
from Tool.cfg_to_dict import cfg_to_dict
from collections.abc import MutableMapping


from Tool.conf_to_dict import conf_to_dict
from Tool.yaml_to_dict import yaml_to_dict

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

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

    output_format = input("Enter the output format, choose 'json' or 'env' ").strip()
    if output_format == "json":
        json_object = json.dumps(output, indent = 4) 
        with open("sample.json", "w") as outfile:
            outfile.write(json_object)

    elif output_format == "env":
        with open("output.env", "w") as f:
            for key, val in output.items():
                f.write(f"{key}={val}\n")
                
        



control_flow()


