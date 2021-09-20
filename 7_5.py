import collections
import os
import shutil


def files_statistic(folder):
    """Returns dict like {size : (count, [extenstion list])}"""
    if not os.listdir(folder):
        raise(FileExistsError)

    result = {}
    for item in os.listdir(folder):
        if not os.path.isdir(os.path.join(folder, item)):
            f_size = os.stat(os.path.join(folder, item)).st_size
            for num in (100, 1_000, 10_000, 100_000):
                if f_size < num:
                    result.setdefault(num, (num, []))
                    result[num] = (result[num][0] + 1,
                                   list(set(result[num][1] + [item.split('.')[1]])))
                    break

    return result


folder = os.path.join(os.getcwd(), 'some_data')
try:
    print(files_statistic(folder))
except FileExistsError:
    print('The folder is empty')
