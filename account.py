class Account:
    def __init__(self,balance):
        self._balance = balance

    def deposit(self, money):
        self._balance += money

    def withraw(self, money):
        self._balance -= money
