class Wallet():
    """Главный класс банка"""
    def __init__(self, name, balance):
        """Инициализация имени и баланса кошельков"""
        self.name = name
        self.balance = balance

    def __str__(self):
        """вывод объектов банка в виде имени и баланса кошелька"""
        return f'{self.name}: {self.balance}'

    def __add__(self, other):
        """функция сложения объектов банка и сумм"""
        if isinstance(other, Wallet):
            new_name = 'Сумарный баланс счетов {s} и {o}'.format(s=self.name, o=other.name)
            if self.traderate <= other.traderate:
                new_balance = self.balance + other.balance * other.traderate
            else:
                new_balance = self.balance + other.balance/other.traderate
        else:
            new_name = self.name
            new_balance = self.balance + float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __radd__(self, other):
        """функция сложения справа"""
        new_name = self.name
        new_balance = self.balance + float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __sub__(self, other):
        """Функция вычитания объектов"""
        if isinstance(other, Wallet):
            new_name = 'Сумарный баланс счетов {s} и {o}'.format(s=self.name, o=other.name)
            if self.traderate <= other.traderate:
                new_balance = self.balance - other.balance * other.traderate
            else:
                new_balance = self.balance - other.balance / other.traderate
        else:
            new_name = self.name
            new_balance = self.balance * self.traderate - float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __mul__(self, other):
        """Функция умножения объектов"""
        new_name = self.name
        new_balance = self.balance * self.traderate * float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __rmul__(self, other):
        """Функция правого умножения объектов"""
        new_name = self.name
        new_balance = self.balance * self.traderate * float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __truediv__(self, other):
        """фенкция деления на число"""
        new_name = self.name
        new_balance = self.balance * self.traderate / float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

class RubleWallet(Wallet):
    """Рублевый кошелек банка"""
    traderate = 1

class DollarWallet(Wallet):
    """Долларовый кошелек банка"""
    traderate = 60

class EuroWallet(Wallet):
    """Евро кошелек банка"""
    traderate = 70

firstwallet = DollarWallet('MyWallet', 6)
secondwallet = RubleWallet('OtherWallet', 220)
thirdwallet = EuroWallet('AnotherWallet', 1)
print(2 * thirdwallet)''''''