class Account:
    def __init__(self,balance):
        self._balance = balance

    def deposit(self, param):
        self._balance += param