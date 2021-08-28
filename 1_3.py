import unittest


def format_procent(num):
    if num % 10 == 1:
        return f"{num} процент"
    elif 20 > num > 10:
        return f"{num} процентов"
    elif num % 10 in (2, 3, 4):
        return f"{num} процента"
    else:
        return f"{num} процентов"


class TestFormatFunc(unittest.TestCase):
    def test1(self):
        self.assertEqual(format_procent(1), "1 процент")

    def test2(self):
        self.assertEqual(format_procent(2), "2 процента")

    def test3(self):
        self.assertEqual(format_procent(54), "54 процента")

    def test4(self):
        self.assertEqual(format_procent(13), "13 процентов")

    def test5(self):
        self.assertEqual(format_procent(5), "5 процентов")

    def test5(self):
        self.assertEqual(format_procent(5), "5 процентов")

    def test6(self):
        self.assertEqual(format_procent(99), "99 процентов")

    def test7(self):
        self.assertEqual(format_procent(101), "101 процент")


if __name__ == "__main__":
    unittest.main()
