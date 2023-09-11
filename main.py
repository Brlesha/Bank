class Wallet():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

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

    def __radd__(self, other):
        new_name = self.name
        new_balance = self.balance + float(other)
        return "{t} {p} руб.".format(t=new_name, p=new_balance)

    def __str__(self):
        return f'{self.name}: {self.balance}'



class RubleWallet(Wallet):
    traderate = 1

class DollarWallet(Wallet):
    traderate = 97

class EuroWallet(Wallet):
    traderate = 105

firstwallet = DollarWallet('MyWallet', 6)
secondwallet = RubleWallet('OtherWallet', 220)
thirdwallet = EuroWallet('AnotherWallet', 3)
print(10 + firstwallet)