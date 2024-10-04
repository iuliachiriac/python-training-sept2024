# 1. Create a BankAccount class that receives two parameters on initialisation:
# bank name (str)
# balance (int)
# 1.A. Create two methods in this class, one to withdraw money and another one
# to deposit money into the account. The withdrawal method will not allow
# withdrawing more money than available: it will print a message and not change
# the balance.

class InsufficientFundsException(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException('insufficient funds')
        self.balance -= amount


# 1.B. Create a BankAccount instance and test the two methods with different
# inputs.
if __name__ == "__main__":
    bank_acc = BankAccount('BRD', 100)  # create instance
    print('Initial balance:', bank_acc.balance)
    bank_acc.deposit(50)  # call deposit() method
    print('Balance after depositing 50:', bank_acc.balance)  # should be 150
    bank_acc.withdraw(70)  # call withdraw() method
    print('Balance after withdrawing 70:', bank_acc.balance)  # should be 80
    try:
        bank_acc.withdraw(100)  # should raise exception
    except InsufficientFundsException as ex:
        print("Trying to withdraw 100:", ex)
    print('Balance after trying to withdraw 100:', bank_acc.balance)
