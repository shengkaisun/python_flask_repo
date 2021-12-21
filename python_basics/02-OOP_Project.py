####################################################
####################################################
# Object Oriented Programming Challenge - Solution
####################################################
####################################################
#
# For this challenge, create a bank account class that has two attributes:
#
# * owner
# * balance
#
# and two methods:
#
# * deposit
# * withdraw
#
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.




class Account():
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Not enough balance.")
            return False
        self.balance -= amount
        return True
    
    def __repr__(self):
        return f"Account owner: {self.owner}, balance: {self.balance}"

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)




# 3. Show the account owner attribute
print(acct1.owner)




# 4. Show the account balance attribute
print(acct1.balance)




# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
print(acct1)



acct1.withdraw(75)
print(acct1)



# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
print(acct1)


# ## Good job!
