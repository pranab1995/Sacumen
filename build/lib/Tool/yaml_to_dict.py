
import yaml
from yaml.loader import FullLoader
# opening a file
def yaml_to_dict(filename):
    with open(filename, 'r') as stream:
        dict1=yaml.load(stream, Loader=FullLoader)
        return dict1

