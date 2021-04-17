class InsufficientFunds(Exception):
    def __init__(self, acct_id, amt_attempted, current_bal):
        self.acct_id = acct_id
        self.amt_attempted = amt_attempted
        self.current_bal = current_bal

    def __str__(self):
        s = "Insufficient funds for {:d}." \
            + "Attempted to withdraw ${:.2f} but only have {:.2f}"
        return s.format(self.acct_id, self.amt_attempted, self.current_bal)

class BankAccount:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0

    def __str__(self):
        return str(self.id) + " Name:" + self.first_name + " " + \
            self.last_name + " Balance: $" + str(self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFunds(self.id,amount, self.balance)
        self.balance -= amount

    def transfer_from(self, amount, to_acct):
        self.withdraw(amount)
        to_acct.deposit(amount)



def main():
    acct1 = BankAccount(123, "Joe", "Smith")
    print('acct1 BEFORE deposit', acct1)
    acct1.deposit(100.00)
    print('acct1 AFTER deposit', acct1)

    try:
        acct1.withdraw(5000.00)
    except InsufficientFunds as e:
        print(e)
    print('acct1 AFTER withdrawal', acct1)

    acct2 = BankAccount(354, "Jane", "Doe")

    # good scenario that'll work
    print('acct1 BEFORE good transfer', acct1)
    print('acct2 BEFORE good transfer', acct2)
    acct1.transfer_from(25.00,acct2)
    print('acct1 AFTER  good transfer', acct1)
    print('acct1 AFTER good transfer', acct2)

    # bad scenario that won't work
    print('acct1 BEFORE bad transfer', acct1)
    print('acct2 BEFORE bad transfer', acct2)
    try:
        acct1.transfer_from(1000.00, acct2)
    except InsufficientFunds as e:
        print(e)
    print('acct1 AFTER bad transfer', acct1)
    print('acct1 AFTER bad transfer', acct2)

main()
