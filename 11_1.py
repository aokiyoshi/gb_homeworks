class Date:
    def __init__(self, date: str):
        self.day, self.month, self.year = self.convert(date)

    @classmethod
    def convert(cls, date: str):
        if not cls.validate(date):
            raise(TypeError('Incorrect date format'))
        return date.split('-')

    @staticmethod
    def validate(date: str) -> bool:
        import re
        if not re.fullmatch(r'([1-9]|[012][0-9]|3[01])-([0]?[1-9]|1[0-2])-\d{4}', date):
            return False
        return True
    
    def __str__(self) -> str:
        return f'{self.day}/{self.month}/{self.year}'
        
            

dates = ('16-04-1992', '02-10-2021', '35-01-2000', '01-16-1045')

for date in dates:
    try:
        print(Date(date))
    except TypeError as err:
        print(err)
