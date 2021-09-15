def hobbies(names, hobs):
    names_file = open(names, 'r', encoding='utf-8')
    hobs_file = open(hobs, 'r', encoding='utf-8')
    names_line = names_file.readline().replace('\n', '')
    hobs_line = hobs_file.readline().replace('\n', '')
    while names_line:
        yield {names_line: hobs_line if hobs_line else None}
        names_line = names_file.readline().replace('\n', '')
        hobs_line = hobs_file.readline().replace('\n', '')
    names_file.close()
    hobs_file.close()
    print(names_file.closed, hobs_file.closed)

print(*hobbies('data/users.csv', 'data/hobby2.csv'), sep='\n')

    

