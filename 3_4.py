from json import dumps


def thesaurus(*args):
    """
    Функция возвращает словарь, в котором ключи - первые буквы имен, а значения - словари, в которых ключи содержат первые буквы имен, 
    а значения массив имен и фамилий
    """
    result = dict()
    for name in args:
        result.setdefault(name.split()[1][0], {}).setdefault(
            name.split()[0][0], []).append(name)
    return result


result = thesaurus('Иван Сергеев', 'Мария Михайлова', 'Петр Алексеев', 'Андрей Смирнов', 'Джеймс Бонд',
                   'Илья Джонс', 'Ильшат Кульбаев', 'Михаил Иванов', 'Полина Алексеева', 'Ирина Серова', sort=False)
# Тут я решил, что функция dumps из библиотеки json справляется с сортировкой лучше, да и выводит в красивом виде.
print(dumps(result, sort_keys=True, indent=2, ensure_ascii=False))
