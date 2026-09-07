class BankAccount:
    acc_no = 0

    def __init__(self,name):
        self.balance = 0
        self.acc_no = self.acc_no + 1
        acc_no = self.acc_no
        self.name = name

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited " + str(amount) + " to " + self.name + "'s account. current balance is " + str(self.balance))

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print(str(amount) + " is withdrawn from " + self.name + "'s account. current balance is " + str(self.balance))
        else:
            print("Not Possible as Balance is " + str(self.balance))

    def print_balance(self):
        print("Balance of " + self.name + " is " + str(self.balance))


if __name__ == '__main__':
    b = BankAccount("Joseph")
    b.deposit(1000)
    b.withdraw(100)
    b.print_balance()

