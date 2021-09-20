import collections
import os
import shutil


def files_statistic(folder):
    """Returns dict like {size : count}"""
    if not os.listdir(folder):
        raise(FileExistsError)

    result = collections.Counter()
    for item in os.listdir(folder):
        if not os.path.isdir(os.path.join(folder, item)):
            f_size = os.stat(os.path.join(folder, item)).st_size
            for num in (100, 1_000, 10_000, 100_000):
                if f_size < num:
                    result[num] += 1
                    break
    return result


folder = os.path.join(os.getcwd(), 'some_data')
try:
    print(files_statistic(folder))
except:
    print('The folder is empty')
