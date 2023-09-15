class table(dict):
    '''класс словаря'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def additem(self, tablo):
        line = input('введите номер строки')
        coloumn = str(input('введите индекс столбца'))
        data = input('Что записываем?')
        index = coloumn + line
        tablo += {index: data}
        return tablo

    def __getitem__(self, item):
        return self.value[item]


a = table({'a': 'b'})
print(a)