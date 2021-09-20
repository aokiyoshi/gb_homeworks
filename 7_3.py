import os
import shutil


def copy_templates(folder):
    """Copies templates from project folder. Raises exception if the folder is empty."""
    if not os.listdir(folder):
        raise(FileExistsError)
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            if item == 'templates':
                shutil.copytree(os.path.join(folder, item), os.path.join(
                    os.getcwd(), 'my_project', 'templates'), dirs_exist_ok=True)
            else:
                copy_templates(os.path.join(folder, item))


folder = r'my_project'
try:
    copy_templates(os.path.join(os.getcwd(), folder))
except FileNotFoundError:
    print(f'Folder "{folder}" is not exsist')
except FileExistsError:
    print(f'Folder "{folder}" is empty')