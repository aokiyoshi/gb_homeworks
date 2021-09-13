def combine(tutor, klass):
    for idx, name in enumerate(tutor):
        yield (name, klass[idx]) if idx < len(klass) else (name, None)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Ильшат'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

print(*combine(tutors, klasses))

print(type(combine(tutors, klasses)))