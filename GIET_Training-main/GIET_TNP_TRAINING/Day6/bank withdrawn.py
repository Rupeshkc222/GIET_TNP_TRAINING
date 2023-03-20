'''
A bank has many customers and each customer has a bank account
There are also privileged customers
who can earn bonus points for each of their transaction.
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- account
__init__(customer_id, customer_name, age, account)
+ withdraw(amount)
+ take_card()
+ get_customer_id()
+ get_customer_name()
+ get_age()
+ get_account()
Account
- account_type
- balance
- min_balance
__init__(account_type,balance,min_balance)
+ get_account_type()
+ get_balance()
+ get_min_balance()
+ set_balance(balance)
PrivilegedCustomer
- bonus_points
__init__ (customer_id, customer_name, age, account,
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the account balance based on the amount withdrawn.
Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than account balance.
LimitReachedException - If the balance amount is less than minimum account balance.
take_card(): Displays the message "Take card out from the ATM".
PrivilegedCustomer:
increase_bonus(): If the account balance is greater than 1000, increase the bonus points by 10, else increase it by 2.
withdraw(amount): Invoke the parent class withdraw() method and increase the bonus points by calling increase_bonus() method, if no exceptions occured.
If exceptions occur, display relevant messages. Ensure that the card is taken out from the ATM under any situation.

Write a Python program to create a new PrivilegedCustomer with below details:
Customer Id: 100
Customer Name: Gopal
Age: 43
Bonus Points: 100
Account Type: Savings
Account Balance: 1000
Account minimum: 500

The customer should be able to withdraw money and also display the bonus points of the customer after the withdraw.
'''
class Account:
    def __init__(self, account_type, balance, min_balance):
        self.account_type = account_type
        self.balance = balance
        self.min_balance = min_balance

    def get_account_type(self):
        return self.account_type

    def get_balance(self):
        return self.balance

    def get_min_balance(self):
        return self.min_balance

    def set_balance(self, balance):
        self.balance = balance

class Customer:
    def __init__(self, customer_id, customer_name, age, account):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.age = age
        self.account = account

    def withdraw(self, amount):
        if amount > self.account.get_balance():
            raise OverdrawException("Withdrawal amount exceeds account balance.")
        elif self.account.get_balance() - amount < self.account.get_min_balance():
            raise LimitReachedException("Account balance would fall below minimum.")
        else:
            self.account.set_balance(self.account.get_balance() - amount)
            print("Withdrawal successful.")

    def take_card(self):
        print("Take card out from the ATM.")

    def get_customer_id(self):
        return self.customer_id

    def get_customer_name(self):
        return self.customer_name

    def get_age(self):
        return self.age

    def get_account(self):
        return self.account


class PrivilegedCustomer(Customer):
    def __init__(self, customer_id, customer_name, age, account, bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.bonus_points = bonus_points

    def increase_bonus(self):
        if self.account.get_balance() > 1000:
            self.bonus_points += 10
        else:
            self.bonus_points += 2

    def withdraw(self, amount):
        try:
            super().withdraw(amount)
            self.increase_bonus()
            print("Withdrawal successful. Bonus points:", self.bonus_points)
        except OverdrawException as e:
            print(e)
        except LimitReachedException as e:
            print(e)
        finally:
            super().take_card()


class OverdrawException(Exception):
    pass


class LimitReachedException(Exception):
    pass


# Creating a new PrivilegedCustomer
account = Account("Savings", 1000, 500)
customer = PrivilegedCustomer(100, "Gopal", 43, account, 100)

# Testing withdrawal and bonus points
customer.withdraw(100)
customer.withdraw(500)
customer.withdraw(1000)