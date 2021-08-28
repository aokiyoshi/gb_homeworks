import unittest


def format_duration(duration):
    days = duration // 86_400
    rem = duration % 86_400
    hours = rem // 3_600
    rem = rem % 3_600
    minutes = rem // 60
    seconds = rem % 60
    return f'{days} д, {hours} ч, {minutes} мин, {seconds} с.'


class TestFormatFunc(unittest.TestCase):

    def test1(self):
        self.assertEqual(format_duration(400_153),
                         '4 д, 15 ч, 9 мин, 13 с.')
    def test2(self):
        self.assertEqual(format_duration(4153),
                         '0 д, 1 ч, 9 мин, 13 с.')
    def test3(self):
        self.assertEqual(format_duration(153),
                         '0 д, 0 ч, 2 мин, 33 с.')
    def test1(self):
        self.assertEqual(format_duration(53),
                         '0 д, 0 ч, 0 мин, 53 с.')
         


if __name__ == '__main__':
    unittest.main()
