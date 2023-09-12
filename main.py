class Wallet():
    """Главный класс банка"""

    def __init__(self, name, balance):
        """Инициализация имени и баланса кошельков"""
        self.name = name
        self.balance = balance

    def __str__(self):
        """вывод объектов банка в виде имени и баланса кошелька"""
        return f'{self.type} {self.name}: {self.balance}'

    def __add__(self, other):
        """функция сложения объектов банка и сумм"""
        if isinstance(other, Wallet):
            new_name = 'Сумарный баланс счетов {s} и {o}'.format(s=self.name, o=other.name)
            if self.traderate <= other.traderate:
                new_balance = self.balance + other.balance * other.traderate
            else:
                new_balance = self.balance + other.balance / self.traderate
        else:
            new_name = self.name
            new_balance = self.balance + float(other)
        return "{t} {p} {c}".format(t=new_name, p=new_balance, c = self.currency)

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

    def __eq__(self, other):
        if isinstance(other, self.__class__) and self.balance * self.traderate == other.balance * other.traderate:
            return True
        else:
            return False

    def spend_all(self):
        if self.balance > 0:
            self.balance -= self.balance
            return self
        else:
            print('баланс не положительный.')

    def to_base(self):
        if not isinstance(self, RubleWallet):
            if self.traderate > 1:
                self.balance = self.balance * self.traderate
            else:
                self.balance = self.balance / self.traderate
        return self




class RubleWallet(Wallet):
    """Рублевый кошелек банка"""
    type = 'Ruble Wallet'
    traderate = 1
    currency = 'руб.'


class DollarWallet(Wallet):
    """Долларовый кошелек банка"""
    type = 'Dollar Wallet'
    traderate = 60
    currency = 'dlr.'


class EuroWallet(Wallet):
    """Евро кошелек банка"""
    type = 'Euro Wallet'
    traderate = 70
    currency = 'eur.'


firstwallet = DollarWallet('MyWallet', 6)
secondwallet = RubleWallet('OtherWallet', 220)
thirdwallet = EuroWallet('AnotherWallet', 1)

"""if EuroWallet('A', 2) == RubleWallet('B', 140):
    print("Хайп")
else:
    print("Кринж")"""

print(DollarWallet("Q", 150) + thirdwallet)