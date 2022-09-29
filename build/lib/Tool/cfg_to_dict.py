
import configparser
config = configparser.ConfigParser()

def cfg_to_dict(filename):
    config.read(filename)
    dict = {}
    for section in config.sections():
        dict[section] = {}
        for option in config.options(section):
            dict[section][option] = config.get(section, option)
    return dict
    


