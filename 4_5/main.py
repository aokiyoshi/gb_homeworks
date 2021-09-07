import sys

import lib


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        print(*lib.find_valute(args[1]), sep='\n')
    else:
        print('Недостаточно аргументов')
