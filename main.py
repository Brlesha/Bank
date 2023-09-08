class Wallet(name, balance, traderate):
    def __init__(self, name, balance, traderate):
        self.name = name
        self.balance = balance * traderate

    def person(self):
        return self.name, self.balance

firstwallet = Wallet('MyWallet', 100, 1)
print(firstwallet.balance)