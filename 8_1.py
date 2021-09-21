import re


def email_parse(email: str) -> dict:
    valid_ext = re.compile(r'(\w+[\.]?\w+)@((\w+[\.]+)+\w+)')
    if valid_ext.match(email) is None:
        raise(ValueError('wrong email:', email))
    result = valid_ext.findall(email)
    return {'username': result[0][0], 'domain': result[0][1]}


print(email_parse('someone@gb.com'))
