def thesaurus(*args, sort=False):
    """
    Функция возвращает словарь, в котором ключи - первые буквы имен, 
    а значения - имена, с  которых они начинаются.
    Если параметр sort равен True, исходный список сначала сортируется, а потом,
    на основе него создается словарь.
    """
    if sort:
       args = sorted(args)
    result = dict()
    for name in args:
        result.setdefault(name[0], []).append(name)
    return result


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья',
      'Ильшат', 'Михаил', 'Полина', 'Андрей', 'Алексей', sort=True))
