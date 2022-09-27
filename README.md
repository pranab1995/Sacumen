# Sacumen
Tool to read .yaml, .cfg, .conf configuration file formats and create JSON or ENV file.


## Requirements

1.Python 3.10.1
2.pyYaml 6.0


<!-- ##To use the tool, you need to implement following commands -->

## To Create a virtual Environment


1. pip install pipenv
2. pipenv shell
3. pipenv install

## Above commands will create a virtual environment and install all the dependencies


## To run the tool
1. CD Tool
2. python main.py

## Command prompt will ask for the input file path. Copy any files absolute path and paste it in the command prompt
## Command prompt will ask for the output file format. Enter the format in which you want the output file to be created.
## Once executed, the output file will be created in the Tool folder

## File information 
1. main.py - Main file to run the tool
2. config.py - Configuration file to read the file
3. config.yaml - Sample yaml file
4. config.cfg - Sample cfg file
5. config.conf - Sample conf file
6. cfg_to_dict.py - File to convert cfg file to dict
7. conf_to_dict.py - File to convert conf file to dict
8. yaml_to_dict.py - File to convert yaml file to dict

## Note: flatten_dict method in main.py file is used to flatten multi level dictionaries, So that it can be converted to JSON or ENV file format