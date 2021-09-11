def odd_to_15():
    for i in range(1,16,2):
        yield i

print(*odd_to_15())