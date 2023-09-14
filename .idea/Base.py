class table():
    """Таблица типо ексель"""
    def __init__(self, index, value):
        """инициализация ячейки таблицы"""
        self.index = frozenset(index)
        self.value = value

    # def write(self):
    #     line = input('введите номер строки')
    #     print(type(line))
    #         if line.type = 'inte'
    #         cloumn = str(input('введите индекс столбца'))
    #
    #
    # def __getitem__(self, item):
    #     if item in self:
    #         return self.value
    #     else:
    #         return print('Эта ячейка пуста')


# action = 'запись'
# while action != 'Закончить':
#     action = input('введите дейтсвие: ')
#     if action == 'запись':
#         table.write()

a = input('Negro')
''''''