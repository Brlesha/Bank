class Wallet():
    def __init__(self, name, balance, traderate):
        self.name = name
        self.balance = balance * traderate

    def person(self):
        return self.name, self.balance

    def __add__(self, other):
        if isinstance(other, Wallet):
            new_title = 'Сумарный баланс счетов {s} и {o}'.format(s=self.name, o=other.name)
            new_price = self.balance + other.balance
        return new_title, new_price

class RubleWallet(Wallet):
    def __init__(self, name, balance, traderate=1):
firstwallet = Wallet('MyWallet', 100, 1)
secondwallet = Wallet('OtherWallet', 200, 1)
print(firstwallet + secondwallet)
