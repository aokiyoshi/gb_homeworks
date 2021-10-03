from collections import defaultdict, Counter


class OfficeEquipStorage:

    # {department: [equip, equip1, equip2...]}
    all_equip = defaultdict(Counter)

    specifications = {}  # {equip_code: EquipData} equip_code is just Manufacturer + Model without any spaces or something between

    def add_to_storage(self, equip, count: int):
        if isinstance(count, int):
            equip_code = equip.manufacturer + equip.model
            self.all_equip['Storage'][equip_code] += count
            self.specifications.setdefault(equip_code, equip)
        else:
                print('Incorrect type of count')
        

    def move_to_dep(self, equip_code, dep: str, count: int):
        if isinstance(count, int):
            if self.all_equip['Storage'][equip_code] >= count:
                self.all_equip[dep][equip_code] += count
                self.all_equip['Storage'][equip_code] -= count
            else:
                print(f'Not enought {equip_code} in the storage')
        else:
            print('Incorrect type of count')

    def show_lineup(self):
        print('Storage:')
        for key, value in self.all_equip['Storage'].items():
            print(key, value)
        print('\n')

    def show_eq_in_dep(self, dep):
        print(f'Equipment in {dep}')
        for key, value in self.all_equip[dep].items():
            print(key, value)
        print('\n')

    def show_model_info(self, eqip_code):
        try:
            print(f'Info about {eqip_code}:\n{self.specifications[eqip_code]}')
        except KeyError:
            print(f'Equipment with code {eqip_code} does not exit')


class OfficeEquip:
    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self) -> str:
        return f'{self.manufacturer}, {self.model}'


class Printer(OfficeEquip):
    def __init__(self, model, manufacturer, type, speed, scanner=False, fax=False):
        super().__init__(model, manufacturer)
        self.type = type
        self.scanner = scanner
        self.fax = fax

    def __str__(self) -> str:
        scanner = 'Yes' if self.scanner else 'No'
        fax = 'Yes' if self.fax else 'No'
        return f'Manucacturer: {self.manufacturer}\nModel: {self.model}\nType: {self.type}\nScanner: {scanner}\nFax: {fax}'


class Scanner(OfficeEquip):
    def __init__(self, model, manufacturer, resolution, apf=False):  # apf = automation pages feed
        super().__init__(model, manufacturer)
        self.resolution = resolution
        self.apf = apf

    def __str__(self) -> str:
        apf = 'Yes' if self.apf else 'No'
        return f'Manucacturer: {self.manufacturer}\nModel: {self.model}\nResolution: {self.resolution} dpi\nAutomated pages feed: {apf}'


class CopyMachine(OfficeEquip):
    def __init__(self, model, manufacturer, colorized=False):
        super().__init__(model, manufacturer)
        self.colorized = colorized

    def __str__(self) -> str:
        color = 'Yes' if self.colorized else 'No'
        return f'Manucacturer: {self.manufacturer}\nModel: {self.model}\nType: {self.type}\nColorized: {color}'


storage_1 = OfficeEquipStorage()

storage_1.add_to_storage(Scanner('289Y', 'Zomy', 10000, False), 10)

storage_1.show_lineup()

storage_1.add_to_storage(CopyMachine('AX-254', 'HT', False), 5)

storage_1.move_to_dep('Zomy289Y', 'IT', 10)

storage_1.move_to_dep('Zomy289Y', 'IT', 10)

storage_1.move_to_dep('Zomy289Y', 'IT', 'blablabla')

storage_1.show_lineup()

storage_1.show_eq_in_dep('IT')

storage_1.show_model_info('Zomy289Y')
