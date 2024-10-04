from solutions.day5_oop_bank_employee import (
    BankAccount,
    Employee,
    InsufficientFundsException,
)


# 5. Create a CreditBankAccount class that inherits BankAccount and receives
# one extra argument at initialisation which allows for the balance to go below
# zero (but not under -overdraft):
# overdraft (int)
# A. Override parent withdraw method so that the new rule is implemented.
class CreditBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft=0):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft:
            raise InsufficientFundsException('overdraft exceeded')
        self._balance -= amount


if __name__ == "__main__":
    # 6. Create an Employee instance that has a CreditBankAccount as its
    # bank_account. Try calling raise_salary and receive_salary on it. Does it
    # behave differently than the first instance?
    cba = CreditBankAccount("ING", 200, 300)
    print('Initial balance:', cba.balance)
    cba.deposit(100)  # call deposit() method
    print('Balance after depositing 100:', cba.balance)  # should be 300
    cba.withdraw(200)  # call withdraw() method
    print('Balance after withdrawing 200:', cba.balance)  # should be 100
    cba.withdraw(200)  # call withdraw() method
    print('Balance after withdrawing another 200:',
          cba.balance)  # should be -100
    try:
        cba.withdraw(250)  # should raise exception
    except InsufficientFundsException as ex:
        print("Trying to withdraw 250:", ex)
    print('Balance after trying to withdraw 250:', cba.balance)

    emp1 = Employee("Jane Doe", cba, 1200)
    print("Initial salary:", emp1.salary)
    print("Initial balance:", emp1.net_worth)
    emp1.raise_salary(10)
    print("Salary after 10% raise:", emp1.salary)
    emp1.receive_salary()
    print("Balance after receiving salary:", emp1.net_worth)
