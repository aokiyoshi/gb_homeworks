def num_translate(word):
    """
    Эта функция переводит цифру на английском на цифру по-русски.
    Если первая буква входного слова заглавня, у перевода тоже будет заглавная
    """
    dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    result = dict.get(word.lower())
    if result and word[0].isupper():
        return result.title()
        
    return result


print(*[num_translate(w)
      for w in ['One', 'one', 'Ten', 'seven', 'Five']], sep=', ')
