class table():
    """Таблица типо ексель"""
    def __init__(self, listing, index, value):
        """инициализация ячейки таблицы"""
        self.index = frozenset(index)
        self.value = value

    def __str__(self):
        return self.listing

    def write(self):
        '''запись в ячейку'''
        line = input('введите номер строки')
        cloumn = str(input('введите индекс столбца'))
        data = input('Что записываем?')


    def __getitem__(self, item):
        if item in self:
            return self.value
        else:
            return print('Эта ячейка пуста')


# action = 'запись'
# while action != 'Закончить':
#     action = input('введите дейтсвие: ')
#     if action == 'запись':
#         table.write()

table =
print(table)