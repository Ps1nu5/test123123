
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Вы пополнили счёт на сумму: {amount} | Текущий баланс: {self.__balance}')
        else:
            print('Величина пополнения должна быть положительной!')

    def withdraw(self, amount):
        
