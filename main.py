class Wallet():
    def __init__(self, name, balance, traderate):
        self.name = name
        self.balance = balance * traderate

    def __add__(self, other):
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

    def __str__(self):
        return f'{self.name}: {self.balance}'

class RubleWallet(Wallet):
    def __init__(self, name, balance, traderate=1):
        self.name = name
        self.balance = balance * traderate

class DollarWallet(Wallet):
    def __init__(self, name, balance, traderate=97):
        self.name = name
        self.balance = balance * traderate

class EuroWallet(Wallet):
    def __init__(self, name, balance, traderate=105):
        self.name = name
        self.balance = balance * traderate

firstwallet = DollarWallet('MyWallet', 6)
secondwallet = RubleWallet('OtherWallet', 200)
thirdwallet = EuroWallet('AnotherWallet', 3)
print(firstwallet + secondwallet)