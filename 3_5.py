from random import choice


def choice2(seq, delete=False):
    """
    Функция возвращает случайный элемент из заданной коллекции.
    Если параметр detele равен True, выбранный элемент будет удален из исходного списка.
    """
    result = choice(seq)
    if delete:
        seq.remove(result)
    return result


def get_jokes(n=1, no_repeat=False):
    """
    Функция возращает заданное количество шуток (комбинаций из слов выбранных случайно из nouns, adverbs и adjectives).
    Если параметр no_repeat равен True, каждое слово из наборов может использоваться лишь один раз. 
    Удаляется после использования.
    При этом, если если n больше чем количество слов в наборах, фунция вернет не больше чем длина этих наборов.
    Если вы какой-то из наборов внутри функции сделаете пустым, функция вернет пустой список.
    """
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    result = []
    for i in range(0, n):
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            break
        noun, adv, adj = choice2(nouns, no_repeat), choice2(
            adverbs, no_repeat), choice2(adjectives, no_repeat)
        result.append(
            ' '.join([noun, adv, adj]))

    print(*result, sep='\n')


print('*' * 4, 'Повторы разрешены:')
get_jokes(10)
print('*' * 4, 'Повторы запрещены, количество шуток больше, чем элементов в наборе:')
get_jokes(10, no_repeat=True)
print('*' * 4, 'Повторы запрещены, количество шуток меньше, чем элементов в наборе:')
get_jokes(2, no_repeat=True)
