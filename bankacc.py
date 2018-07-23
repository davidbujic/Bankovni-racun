class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Vlasnik racuna: %s; Stanje: %.2f dinara." % (self.name, self.balance)

    def show_balance(self):
        print "Stanje: %.2f" % self.balance

    def deposit(self, amount):
        if amount <= 0:
            print "Depozit mora biti pozitivna vrednost."
            return
        print "Vrednost depozita: %.2f dinara." % amount
        self.balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print "Nedovoljno sredstava za podizanje %.2f dinara;" % amount,
            self.show_balance()
            return
        print "Vrednost podizanja: %.2f dinara." % amount
        self.balance -= amount
        self.show_balance()

my_account = BankAccount("David Bujic")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.deposit(0)
my_account.withdraw(1000)
print my_account
my_account.withdraw(1001)
            
