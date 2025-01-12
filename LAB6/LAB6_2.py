class Bank:
    def __init__(self):
        self.__user_list = []
        self.__atm_list = []
        self.__card_list = []

    @property
    def user_list(self):
        return self.__user_list
    
    @property
    def atm_list(self):
        return self.__atm_list
    
    @property
    def card_list(self):
        return self.__card_list

class ATM:
    atm_money = 1000000
    limit_money = 40000

    def __init__(self, atm_id):
        self.__atm_id = atm_id

    @property
    def atm_id(self):
        return self.__atm_id
    
    def insert_card(self, card, account, pin_number):
        if pin_number == card.pin_number:
            return card, account
        return None, None
    
    def deposit(self, account, money):
        if money <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        account.balance += money
        transaction = Transaction('D-ATM', money, account.balance, '30-12-2023', self.atm_id, account.account_id)
        account.transaction_list.append(transaction)
        return "Success"
    
    def withdraw(self, account, money):
        if money <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if money > account.balance:
            raise ValueError("Insufficient funds.")
        
        account.balance -= money
        transaction = Transaction('W-ATM', money, account.balance, '30-12-2023', self.atm_id, account.account_id)
        account.transaction_list.append(transaction)
        return "Success"
    
    def transfer(self, account1, account2, money):
        if money <= 0:
            raise ValueError("Transfer amount must be positive.")
        if money > account1.balance:
            raise ValueError("Insufficient funds.")
        
        account1.balance -= money
        account2.balance += money
        
        transaction1 = Transaction('T-ATM', money, account1.balance, '30-12-2023', self.atm_id, account1.account_id)
        transaction2 = Transaction('T-ATM', money, account2.balance, '30-12-2023', self.atm_id, account2.account_id)
        
        account1.transaction_list.append(transaction1)
        account2.transaction_list.append(transaction2)
        
        return "Success"

class DebitCard:
    def __init__(self, card_no, account_id):
        self.__card_no = card_no
        self.__account_id = account_id

    @property
    def card_no(self):
        return self.__card_no
    
    @property
    def account_id(self):
        return self.__account_id

class DepositAccount:
    def __init__(self, account_id, user, balance, interest_rate):
        self.__account_id = account_id
        self.__user = user
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transaction_list = []

    @property
    def account_id(self):
        return self.__account_id
    
    @property
    def user(self):
        return self.__user
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    @property
    def interest_rate(self):
        return self.__interest_rate

    @property
    def transaction_list(self):
        return self.__transaction_list

class User:
    def __init__(self, citizen_id, name):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__account_list = []

    @property
    def citizen_id(self):
        return self.__citizen_id

    @property
    def name(self):
        return self.__name
    
    @property
    def account_list(self):
        return self.__account_list

class Transaction:
    def __init__(self, type, money, balance, time, atm_id, account_id):
        self.__type = type
        self.__money = money
        self.__balance = balance
        self.__time = time
        self.__atm_id = atm_id
        self.__account_id = account_id
      
    def __str__(self):
        if self.__type == 'D-ATM':
            return f"{self.__type} : {self.__atm_id}- +{self.__money}-{self.__balance}"
        elif self.__type == 'W-ATM':
            return f"{self.__type} : {self.__atm_id}- -{self.__money}-{self.__balance}"
        elif self.__type == 'T-ATM':
            return f"{self.__type} : {self.__atm_id}- -{self.__money}-{self.__balance}"
        elif self.__type == 'P':
            return f"{self.__type} : -{self.__money}"
        else:
            return "Unknown Transaction Type"

    @property
    def type(self):
        return self.__type
    
    @property
    def money(self):
        return self.__money

    @property
    def balance(self):
        return self.__balance
    
    @property
    def time(self):
        return self.__time
    
    @property
    def atm_id(self):
        return self.__atm_id
    
    @property
    def account_id(self):
        return self.__account_id

# Example Usage:

bank = Bank()

user3 = User('1-1101-12345-14-0', 'Ron Weasley')
account3 = DepositAccount('1357913579', user3, 5000, 0.03)
debit_card3 = DebitCard('54321', '1357913579')

# Adding the new user and their account to the bank's records
bank.user_list.append(user3)
bank.card_list.append(debit_card3)

# Performing transactions (deposit, withdrawal, transfer)
atm1 = ATM('1001')
atm2 = ATM('1002')

atm1.deposit(account3, 2000)
atm2.withdraw(account3, 1000)
account4 = DepositAccount('246813579', user3, 10000, 0.04)
atm2.transfer(account3, account4, 3000)

# Printing out the transaction history
for transaction in account3.transaction_list:
    print(transaction)

for transaction in account4.transaction_list:
    print(transaction)