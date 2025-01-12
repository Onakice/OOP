from typing import Any


class Bank:

    def __init__(self,name):
        self.__name=name
        self.__user_list = []
        # self.__card_list = []
        self.__atm_list = []
        self.__seller_list = []

    @property
    def user_list(self):
        return self.__user_list
    
    @property
    def card_list(self):
        return self.__card_list
    
    @property
    def atm_list(self):
        return self.__atm_list

    @property
    def seller_list(self):
        return self.__seller_list


    def add_user(self, user):
        self.__user_list.append(user)

    # def add_card(self, typeCard):
    #     self.__card_list.append(typeCard)

    # def add_atm(self, atm):
    #     self.__atm_list.append(atm)
        
    def add_atm_machine(self, atm_machine):
        self.__atm_list.append(atm_machine)

    def add_seller(self, sellerer):
        self.seller_list.append(sellerer)

    def search_atm_machine(self, atm_id):
        for machinenum in self.__atm_list:
            if machinenum.atm_no == atm_id:
                return machinenum
        return None

    # def search_user_from_id(self, citizen_id):
    #     for users in self.user_list:
    #         if citizen_id == users.citizen_id:
    #             return True
        
    def search_user_from_id(self, citizen_id):
        for user in self.__user_list:
            if user.citizen_id == citizen_id:
                return user
        return None
    
    # def search_account_from_card(self, numcard):
    #     for user in self.__user_list:
    #         if user.account_no == numcard:
    #             return user
    #     return None

    # def search_account_from_card(self, card_number):
    #     for user in self.__user_list:
    #         for account in user.account_list:
    #             for card in account.card_list:
    #                 if card.card_no == card_number:
    #                     return account
    #     return None

    # def search_account_from_card(self, card_number):
    #     for user in self.__user_list:
    #         for account in user.account_list:
    #             if isinstance(account, SavingAccount):
    #                 if account.card and account.card.card_no == card_number:
    #                     return account
    #             else:
    #                 for card in account.card_list:
    #                     if card.card_no == card_number:
    #                         return account
    #     return None

    # def search_account_from_card(self, card_number):
    #     for user in self.__user_list:
    #         for account in user.account_list:
    #             if isinstance(account, Account):
    #                 if isinstance(account, SavingAccount) and account.card and account.card.card_no == card_number:
    #                     return account
    #                 elif isinstance(account, SavingAccount):
    #                     for card in account.card_list:
    #                         if card.card_no == card_number:
    #                             return account
    #                 elif isinstance(account, FixDepositAccount):
    #                     # Skip accessing card attribute for FixDepositAccount
    #                     continue
    #     return None

    def search_account_from_card(self, card_no):
        for user in self.__user_list:
            for account in user.account_list:
                if account.card.card_no == card_no:
                    return account
        return None
        
    
    def search_account_from_account_no(self, account_no):
        for user in self.__user_list:
            for account in user.account_list:
                if account.account_no == account_no:
                    return account
        return None
       
    def search_seller(self, seller_name):
        for sellers in self.seller_list: 
            if sellers.name == seller_name:
                return sellers
        return None
    

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

    # def add_account(self, account_no, user, amount):
    #     self.__account_no.append(account_no, user, amount)

    def add_account(self, account):
        self.__account_list.append(account)

    # def add_user(self, user):
    #     self.__user_list.append(user)
    
    def search_account(self, id):
        for accounts in self.account_list:
            if accounts.account_no == id:
                return accounts
        return None
    
 

class Account:
    def __init__(self, account_no, user, amount):
        self.__account_no = account_no
        self.__user = user
        self.__amount = amount
        self.__transaction = []
        self.__card_list = []

    @property
    def account_no(self):
        return self.__account_no
    
    @property
    def user(self):
        return self.__user
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @property
    def transaction(self):
        return self.__transaction
    
    @property
    def card_list(self):
        return self.__card_list
    
    def __add__(self, amount):
        self.__amount += amount
        self.__transaction.append(Transaction("Deposit", amount, self.__amount, None))

    def __sub__(self, amount):
        self.__amount -= amount
        self.__transaction.append(Transaction("Withdraw", amount, self.__amount, None))
    
    def __irshift__(self, payload):
        amount = payload[0]
        target_account = payload[1]
        if not isinstance(amount, int) and not isinstance(amount, float and amount > self.__amount and amount < 0) and not isinstance(target_account, Account): return "Error"
        self.__amount -= amount
        target_account.__amount += amount
        self.__transaction.append(Transaction("out_tranfer", amount, self.__amount, target_account))
        target_account.__transaction.append(Transaction("come_tranfer", amount, target_account.__amount, self))

    def transfer(self, account, amount, target_account):
        account >>= (amount, target_account)

    # def add_card(self, typecard):
    #     self.__card_list.append(typecard)

    # def get_card(self):
    #     if self.__card_list:
    #         return self.__card_list[0]
    #     else:
    #         return None

    # def __iter__(self):
    #     return iter(self.__transaction)

    # def get_card(self, typecard):
    #     return typecard(self.__account_no, self, '1234')



class SavingAccount(Account):

    interest_rate = 0.5
    type = "Saving"

    def __init__(self, account_no, user, amount):
        Account.__init__(self, account_no, user, amount)
        self.__card = None

    def add_card(self, card):
        self.__card = card

    def get_card(self):
        return self.__card

    @property
    def card(self):
        return self.__card

    # def set_balance(self, new_balance):
    #     self._Account__amount = new_balance

class FixDepositAccount(Account):

    interest_rate = 2.5

class Transaction:
    def __init__(self, transaction_type, amount, total, target_account):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__total = total
        self.__target_account = target_account

    @property
    def transaction_type(self):
        return self.__transaction_type

class Card:
    def __init__(self,card_no, account, pin):
        self.__card_no = card_no
        self.__account = account
        self.__pin = pin

    @property
    def card_no(self):
        return self.__card_no
    
    @property
    def account(self):
        return self.__account
    
    @property
    def pin(self):
        return self.__pin

class ATM_Card(Card):

    fee = 150

class Debit_Card(Card):

    fee = 300

class ATM_machine:

    withdraw_limit = 20000

    def __init__(self,atm_no,money):
        self.__atm_no = atm_no
        self.__money = money

    @property
    def atm_no(self):
        return self.__atm_no

    def insert_card(self, card, pin):
        if atm_card.pin == pin:
            return "Success"
        return None
    
    # def insert_card(self, card, pin):
    #     if card.pin == pin:
    #         return "Success"
    #     return None
    
    # def set_balance(self, new_balance):
    #     self._Account__amount = new_balance

    # def deposit(self, account, amount):
    #     if amount > 0:
    #         account.set_balance += amount
    #         account.transaction_list.append(Transaction('D-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         print("Deposit ",amount)
    #     return "Error class ATM_machine def deposit"

    # def deposit(self, account, amount):
    #     if amount > 0:
    #         account.set_balance(account.amount + amount)
    #         self.transaction_list.append(Transaction('D-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         print("Deposit ", amount)
    #         return "Success"
    #     return "Error class ATM_machine def deposit"
    
    def deposit(self, account, amount):
        account += amount
        self.__money += amount

    def withdraw(self, account, amount):
        if amount <= self.withdraw_limit and amount <= self.__money:
            account -= amount
            self.__money -= amount

    def transfer(self, account, amount, target_account):
        account >> target_account, amount

    # def deposit(self, account, amount):
    #     if amount > 0:
    #         account.set_balance(account.amount + amount)
    #         if hasattr(account, 'transaction_list'):
    #             account.transaction_list.append(Transaction('D-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         print("Deposit ", amount)
    #         return "Success"
    #     return "Error: Invalid deposit amount at class ATM_machine def deposit"

    # def deposit(self, account, amount, atm_id):
    #     if amount > 0:
    #         account._Account__amount += amount  # Directly access and update the amount property
    #         # Assuming transaction_list is a property of the account, you may need to adjust this part if it's different
    #         account.transaction.append(Transaction('D-ATM', amount, account.amount, '30-12-2023', atm_no, account.account_id))
    #         return "Success"
    #     return "Error class ATM_machine def deposit"

    # def withdraw(self, account, amount):
    #     if amount > account.balance:
    #         return "Error class ATM_machine def withdraw 1"
    #     elif amount > 0:
    #         account.set_balance -= amount
    #         account.transaction_list.append(Transaction('W-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         return account.balance
    #     return "Error class ATM_machine def withdraw 2"
    
    # def withdraw(self, account, amount):
    #     if amount > account.amount:
    #         return "Error class ATM_machine def withdraw 1"
    #     elif amount > 0:
    #         account.set_balance(account.amount - amount)
    #         account.transaction_list.append(Transaction('W-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         return account.amount
    #     elif amount > self.withdraw_limit:
    #         return "Error amount > withdraw_limit"
    #     return "Error class ATM_machine def withdraw 2"
    
    # def withdraw(self, account, amount):
    #     if amount > account.amount:
    #         return "Error class ATM_machine def withdraw 1"
    #     elif amount > 0:
    #         account.set_balance(account.amount - amount)
    #         if hasattr(account, 'transaction_list'):
    #             account.transaction_list.append(Transaction('W-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         return account.amount
    #     elif amount > self.withdraw_limit:
    #         return "Error amount > withdraw_limit"
    #     return "Error class ATM_machine def withdraw 2"


    # def transfer(self,account, amount, target_account):
    #     if amount > account.balance:
    #         return "Error class ATM_machine def transfer"
    #     elif amount > 0:
    #         account.set_balance -= amount
    #         target_account.set_balance += amount
    #         account.transaction_list.append(Transaction('T-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #         target_account.transaction_list.append(Transaction('T-ATM', amount, target_account.balance, '30-12-2023', atm.atm_id, target_account.account_id))
    #         return "Error class ATM_machine def transfer 2"
        
    # def transfer(self,account, amount, target_account):
    #     if amount > account.amount:
    #         return "Error class ATM_machine def transfer"
    #     elif amount > 0:
    #         account.set_balance(account.amount - amount)
    #         target_account.set_balance(target_account.amount + amount)
    #         if hasattr(account, 'transaction_list'):
    #             account.transaction_list.append(Transaction('T-ATM', amount, account.balance, '30-12-2023', atm.atm_id, account.account_id))
    #             target_account.transaction_list.append(Transaction('T-ATM', amount, target_account.balance, '30-12-2023', atm.atm_id, target_account.account_id))
    #         return "Success"
    #     return "Error class ATM_machine def transfer 2"

    # def transfer(self, account, amount, target_account):
    #     if amount > account.amount:
    #         return "Error: Insufficient balance"
    #     elif amount > 0:
    #         account.set_balance(account.amount - amount)
    #         target_account.set_balance(target_account.amount + amount)
    #         if hasattr(account, 'transaction_list') and hasattr(target_account, 'transaction_list'):
    #             account.transaction_list.append(Transaction('T-ATM', amount, account.balance, '30-12-2023', self.atm_no, account.account_no))
    #             target_account.transaction_list.append(Transaction('T-ATM', amount, target_account.balance, '30-12-2023', self.atm_no, target_account.account_no))
    #         return "Success"
    #     return "Error: Invalid transfer amount"


class Seller:
    def __init__(self,seller_no,name):
        self.__seller_no = seller_no
        self.__name = name
        self.__edc_list = []

    @property
    def seller_no(self):
        return self.__seller_no
    
    @property
    def name(self):
        return self.__name
    
    @property
    def edc_list(self):
        return self.__edc_list
    
    def add_edc(self, edc):
        if not isinstance(edc, EDC_machine): return "Error"
        self.edc_list.append(edc)

    def search_edc_from_no(self, edc_no):
        if not isinstance(edc_no, str): return "Error"
        for edcs in self.edc_list:
            if edcs.edc_no == edc_no:
                return edcs
        return None
    
    def paid(self, account, amount, target_account):
        account >>= (amount, target_account)

    # def paid(self, account, amount, target_account):
    #     if amount <= account.amount:
    #         account.set_balance(account.amount - amount)
    #         target_account.set_balance(target_account.amount + amount)
    #         return True
    #     else:
    #         return False
    

class EDC_machine:
    def __init__(self,edc_no,seller):
        self.__edc_no = edc_no
        self.__seller = seller

    @property
    def edc_no(self):
        return self.__edc_no

    def paid(self, debit_card, amount, target_account):
        tempAcc = debit_card.account
        tempAcc >>= (amount, target_account)

    # def paid(self, card, amount, seller_account):
    #     if self.verify_card(card) and amount > 0:
    #         if card.account.amount >= amount:
    #             card.account.set_balance(card.account.amount - amount)
    #             seller_account.set_balance(seller_account.amount + amount)
    #             # print("Payment successful.")
    #             return True
    #         else:
    #             print("Insufficient funds.")
    #     else:
    #         print("Invalid card or amount.")
    #     return False
    
    def verify_card(self, card):
        return True


##################################################################################

# กำหนด รูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, ประเภทบัญชี, หมายเลขบัญชี, จำนวนเงินในบัญชี, ประเภทบัตร, หมายเลขบัตร ]}
user ={'1-1101-12345-12-0':['Harry Potter','Savings','1234567890',20000,'ATM','12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Saving','0987654321',1000,'Debit','12346'],
       '1-1101-12345-13-0':['Hermione Jean Granger','Fix Deposit','0987654322',1000,'',''],
       '9-0000-00000-01-0':['KFC','Savings','0000000321',0,'',''],
       '9-0000-00000-02-0':['Tops','Savings','0000000322',0,'','']}

atm ={'1001':1000000,'1002':200000}

seller_dic = {'210':"KFC", '220':"Tops"}

EDC = {'2101':"KFC", '2201':"Tops"}

# TODO 1 : สร้าง Instance ของธนาคาร และ สร้าง Instance ของ User, Account, บัตร
# TODO   : จากข้อมูลใน user รูปแบบการนำข้อมูลไปใช้สามารถใช้ได้โดยอิสระ
# TODO   : โดย Account แบ่งเป็น 2 subclass คือ Savings และ FixedDeposit
# TODO   : โดย บัตร แบ่งเป็น 2 subclass คือ ATM และ Debit

scb = Bank('SCB')
scb.add_user(User('1-1101-12345-12-0','Harry Potter'))
scb.add_user(User('1-1101-12345-13-0','Hermione Jean Granger'))
scb.add_user(User('9-0000-00000-01-0','KFC'))
scb.add_user(User('9-0000-00000-02-0','Tops'))
harry = scb.search_user_from_id('1-1101-12345-12-0')
harry.add_account(SavingAccount('1234567890', harry, 20000))
harry_account = harry.search_account('1234567890')
harry_account.add_card(ATM_Card('12345', harry, '1234'))
hermione = scb.search_user_from_id('1-1101-12345-12-0')
hermione.add_account(SavingAccount('0987654321',hermione,2000))
hermione_account1 = hermione.search_account('0987654321')
hermione_account1.add_card(Debit_Card('12346',hermione_account1,'1234'))
hermione.add_account(FixDepositAccount('0987654322',hermione,1000))
kfc = scb.search_user_from_id('9-0000-00000-01-0')
kfc.add_account(SavingAccount('0000000321', kfc, 0))
tops = scb.search_user_from_id('9-0000-00000-02-0')
tops.add_account(SavingAccount('0000000322', tops, 0))

# TODO 2 : สร้าง Instance ของเครื่อง ATM

scb.add_atm_machine(ATM_machine('1001',1000000))
scb.add_atm_machine(ATM_machine('1002',200000))

# TODO 3 : สร้าง Instance ของ Seller และใส่เครื่อง EDC ใน Seller 

temp = Seller('210','KFC')
temp.add_edc(EDC_machine('2101',temp))
scb.add_seller(temp)
temp = Seller('220',"Tops")
temp.add_edc(EDC_machine('2201',temp))
scb.add_seller(temp)

# TODO 4 : สร้าง method ฝาก โดยใช้ __add__ ถอน โดยใช้ __sub__ และ โอนโดยใช้ __rshift__
# TODO   : ทดสอบการ ฝาก ถอน โอน โดยใช้ + - >> กับบัญชีแต่ละประเภท

# TODO 5 : สร้าง method insert_card, deposit, withdraw และ transfer ที่ตู้ atm และเรียกผ่าน account อีกที
# TODO   : ทดสอบโอนเงินระหว่างบัญชีแต่ละประเภท

# TODO 6 : สร้าง method paid ที่เครื่อง EDC และเรียกผ่าน account อีกที

# TODO 7 : สร้าง method __iter__ ใน account สำหรับส่งคืน transaction เพื่อให้ใช้กับ for ได้ 

# Test case #1 : ทดสอบ การฝาก จากเครื่อง ATM โดยใช้บัตร ATM ของ harry
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method deposit จากเครื่อง ATM และเรียกใช้ + จาก account
# ผลที่คาดหวัง :
# Test Case #1
# Harry's ATM No :  12345
# Harry's Account No :  1234567890
# Success
# Harry account before deposit :  20000
# Deposit 1000
# Harry account after deposit :  21000

atm_machine = scb.search_atm_machine('1001')
harry_account = scb.search_account_from_card('12345')
atm_card = harry_account.get_card()
print("Test Case #1")
print("Harry's ATM No : ",atm_card.card_no)
print("Harry's Account No : ",harry_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Harry account before deposit : ",harry_account.amount)
print("Deposit 1000")
atm_machine.deposit(harry_account,1000)
print("Harry account after deposit : ",harry_account.amount)
print("")

# Test case #2 : ทดสอบ การถอน จากเครื่อง ATM โดยใช้บัตร ATM ของ hermione
# ต้องมีการ insert_card ก่อน ค้นหาเครื่อง atm เครื่องที่ 2 และบัตร atm ของ hermione
# และเรียกใช้ function หรือ method withdraw จากเครื่อง ATM และเรียกใช้ - จาก account
# ผลที่คาดหวัง :
# Test Case #2
# Hermione's ATM No :  12346
# Hermione's Account No :  0987654321
# Success
# Hermione account before withdraw :  2000
# withdraw 1000
# Hermione account after withdraw :  1000

atm_machine = scb.search_atm_machine('1002')
hermione_account = scb.search_account_from_card('12346')
atm_card = hermione_account.get_card()
print("Test Case #2")
print("Hermione's ATM No : ", atm_card.card_no)
print("Hermione's Account No : ", hermione_account.account_no)
print(atm_machine.insert_card(atm_card, "1234"))
print("Hermione account before withdraw : ",hermione_account.amount)
print("withdraw 1000")
atm_machine.withdraw(hermione_account,1000)
print("Hermione account after withdraw : ",hermione_account.amount)
print("")


# Test case #3 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ที่เคาน์เตอร์
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง
# Test Case #3
# Harry's Account No :  1234567890
# Hermione's Account No :  0987654321
# Harry account before transfer :  21000
# Hermione account before transfer :  1000
# Harry account after transfer :  11000
# Hermione account after transfer :  11000

harry_account = scb.search_account_from_card('12345')
hermione_account = scb.search_account_from_card('12346')
print("Test Case #3")
print("Harry's Account No : ",harry_account.account_no)
print("Hermione's Account No : ", hermione_account.account_no)
print("Harry account before transfer : ",harry_account.amount)
print("Hermione account before transfer : ",hermione_account.amount)

# harry_account.transfer("0000", 10000, hermione_account)
harry_account.transfer(harry_account, 10000, hermione_account)
# atm_machine.transfer(harry_account, 10000, hermione_account)

print("Harry account after transfer : ",harry_account.amount)
print("Hermione account after transfer : ",hermione_account.amount)
print("")

# Test case #4 : ทดสอบการชำระเงินจากเครื่องรูดบัตร ให้เรียกใช้ method paid จากเครื่องรูดบัตร
# โดยให้ hermione ชำระเงินไปยัง KFC จำนวน 500 บาท ผ่านบัตรของตัวเอง
# ผลที่คาดหวัง
# Hermione's Debit Card No :  12346
# Hermione's Account No :  0987654321
# Seller :  KFC
# KFC's Account No :  0000000321
# KFC account before paid :  0
# Hermione account before paid :  11000
# KFC account after paid :  500
# Hermione account after paid :  10500

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
kfc_account = scb.search_account_from_account_no('0000000321')
kfc = scb.search_seller('KFC')
edc = kfc.search_edc_from_no('2101')

print("Test Case #4")
print("Hermione's Debit Card No : ", debit_card.card_no)
print("Hermione's Account No : ",hermione_account.account_no)
print("Seller : ", kfc.name)
print("KFC's Account No : ", kfc_account.account_no)
print("KFC account before paid : ",kfc_account.amount)
print("Hermione account before paid : ",hermione_account.amount)
edc.paid(debit_card, 500, kfc_account)
print("KFC account after paid : ",kfc_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")

# Test case #5 : ทดสอบการชำระเงินแบบอิเล็กทรอนิกส์ ให้เรียกใช้ method paid จาก kfc
# โดยให้ Hermione ชำระเงินไปยัง Tops จำนวน 500 บาท
# ผลที่คาดหวัง
# Test Case #5
# Hermione's Account No :  0987654321
# Tops's Account No :  0000000322
# Tops account before paid :  0
# Hermione account before paid :  10500
# Tops account after paid :  500
# Hermione account after paid :  10000

hermione_account = scb.search_account_from_account_no('0987654321')
debit_card = hermione_account.get_card()
tops_account = scb.search_account_from_account_no('0000000322')
tops = scb.search_seller('Tops')
print("Test Case #5")
print("Hermione's Account No : ",hermione_account.account_no)
print("Tops's Account No : ", tops_account.account_no)
print("Tops account before paid : ",tops_account.amount)
print("Hermione account before paid : ",hermione_account.amount)

tops.paid(hermione_account,500,tops_account)
# EDC_machine.paid(debit_card, 500, tops_account)

print("Tops account after paid : ",tops_account.amount)
print("Hermione account after paid : ",hermione_account.amount)
print("")


# # Test case #7 : แสดง transaction ของ Hermione ทั้งหมด โดยใช้ for loop 

