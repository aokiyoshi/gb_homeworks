import os
import shutil

import yaml


def dir_from_dict(input_dict, path=''):
    """Makes folders tree from YAML config file"""
    for key in input_dict.keys():

        root_path = os.path.join(path, key)
        os.mkdir(root_path) # Make root path from config file
        current_val = input_dict[key]

        # If current value is dict we should do recursion
        if isinstance(current_val, dict): 
            dir_from_dict(current_val, root_path)
        else:
            for fold in current_val:
                # Another recursion in case, when current value is dict 
                if isinstance(fold, dict):
                    dir_from_dict(fold, root_path)
                else:
                    with open(os.path.join(root_path, fold), 'x') as f:
                        f.write('')


with open('data/config.yaml') as f:
    result = yaml.safe_load(f)

dir_from_dict(result, os.getcwd())
