from typing import Self, Type

class BankAccount:
    def __init__(self, name:str='John', balance:float=1000):
        self.name = name
        self.balance = balance

    def deposit(self, amount:float) -> None:
        self.balance += amount

    def withdraw(self, amount:float) -> None:
        if amount > self.balance:
            print('Vous n\'avez assez')
            return

        self.balance -= amount
        # self.balance = self.balance - amount

    def transfer(self, destination:Type[Self], amount:float):
        if amount > self.balance:
            print('Vous n\'avez assez')
            return

        self.balance -= amount
        destination += amount
        
    def __str__(self) -> str:
        return f'{self.name} - {self.balance}'
    
class SavingsAccount(BankAccount):
    def __init__(self, 
                 name:str='John', 
                 balance:float=1000, 
                 monthly_rate:float=0.3):
        BankAccount.__init__(self, name, balance)
        self.monthly_rate = monthly_rate / 100

    def set_rate(self, monthly_rate: float) -> None:
        self.monthly_rate = monthly_rate / 100

    def capitalization(self, month_count:int) -> None:
        self.balance *= (1 + self.monthly_rate) ** month_count
        # self.balance = self.balance * ((1 + self.monthly_rate) ** month_count)

    def __str__(self) -> str:
        return f"Name : {self.name} \nBalance : {self.balance:.2f} \nRate : {self.monthly_rate*100}%"

if __name__ == "__main__":
    jane_account = SavingsAccount('Jane', 1000, 0.3)
    jane_account.capitalization(12)
    print(jane_account)


# alice_account = BankAccount(name='Alice', balance=2200)
# john_account = BankAccount()
# print(alice_account)