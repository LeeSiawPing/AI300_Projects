# In-Class Practice: Write your own class from scratch

class CreditCard:
    
    def __init__(self,account_number, credit_limit):
        # instance attributes
        self.account_number = account_number
        self.__credit_limit = credit_limit
        self.__balance = 0
        # use __ to show that private variables that should only change in the class
    
    def get_balance(self):
        return self.__balance

    def get_credit_limit(self):
        return self.__credit_limit

    def set_credit_limit(self, new_credit_limit):
        if new_credit_limit < 0:
            print("Credit limit cannot be less than 0")
        elif  new_credit_limit > 100000:
             print("Credit limit cannot be more than 100000")
        else:
            self.__credit_limit = new_credit_limit

    def make_purchase(self, amount):
        if amount < 0:
            print("Purchase amount cannot be less than 0")
        elif self.__credit_limit - self.__balance < amount:
            print ("Insufficient balance")
        else:
            self.__balance += amount
    
    def make_payment(self,payment):
        if payment < 0:
            print("Payment amount cannot be less than 0")
        elif payment > self.__balance:
            self.__balance = 0
        else:
            self.__balance -= payment


# Uncomment each test to experiment with your class once completed!

my_credit_card = CreditCard(123456789, 5000)
print("My credit info is "+ str(my_credit_card.account_number) + " and " + str(my_credit_card.get_credit_limit()))

##The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
assert my_credit_card.account_number == 123456789
assert my_credit_card.get_balance() == 0
assert my_credit_card.get_credit_limit() == 5000

my_credit_card.set_credit_limit(1000)
print("My credit info is "+ str(my_credit_card.account_number) + " and " + str(my_credit_card.get_credit_limit()))

my_credit_card.set_credit_limit(-1)       # print error
my_credit_card.set_credit_limit(100001)   # print error
assert my_credit_card.get_credit_limit() == 1000

my_credit_card.make_purchase(900)
my_credit_card.make_purchase(-1)          # print error
my_credit_card.make_purchase(200)         # print error
assert my_credit_card.get_balance() == 900


# Optional Tests: implement Make Payment functionality
my_credit_card.make_payment(500)
assert my_credit_card.get_balance() == 400
my_credit_card.make_payment(5000)
assert my_credit_card.get_balance() == 0
my_credit_card.make_payment(-200)

print("All tests passed!")
