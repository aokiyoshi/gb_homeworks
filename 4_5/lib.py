import datetime

from requests import get, utils


def find_between(text: str, start: str, end: str):
    start_index = text.find(start)
    if start_index == -1:
        return ''
    end_index = text.find(end, start_index)
    return text[start_index + len(start): end_index]


def find_valute(code: str):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    valute = find_between(find_between(content, code.upper(), '</Value>'), '<Value>', '*')
    day, month, year = [int(num) for num in find_between(content, 'Date="', '" name').split('.')]
    if not valute:
        return (None, datetime.date(year, month, day))
    return (float(valute.replace(',', '.')), datetime.date(year, month, day))


