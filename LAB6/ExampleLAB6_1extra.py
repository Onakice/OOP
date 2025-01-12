# Class Code

##################################################################################

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

    
# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

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
   
   def insert_card(self,account,card, pin_number):
      if pin_number == card.pin_number:
         return print(account.account_id,card.card_no,"Success")
      return None
   
   def deposit(self,atm, account, money):
      if money > 0:
         account.set_balance += money
         account.transaction_list.append(Transaction('D-ATM',money,account.balance,'30-12-2023',atm.atm_id,account.account_id))
      return "Error"

   def withdraw(self, atm, account, money):
      if money > account.balance:
         return "Error"
      elif money > 0:
         account.set_balance -= money
         account.transaction_list.append(Transaction('W-ATM',money,account.balance,'30-12-2023',atm.atm_id,account.account_id))
         return account.balance
      return "Error"
      
   def transfer(self, atm, account1, account2, money):
      if money > account1.balance:
         return "Error"
      elif money > 0:
         account1.set_balance -= money
         account2.set_balance += money
         account1.transaction_list.append(Transaction('T-ATM',money,account1.balance,'30-12-2023',atm.atm_id,account1.account_id))
         account2.transaction_list.append(Transaction('T-ATM',money,account2.balance,'30-12-2023',atm.atm_id,account2.account_id))
         return account1.balance, account2.balance
      return "Error"

class User:
   def __init__(self, citizen_id, name,):
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
    
class Account:
   def __init__(self, account_id, user, balance):
      self.__account_id = account_id
      self.__user = user
      self.__balance = balance
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
   def set_balance(self, balance):
      self.__balance = balance

   @property
   def transaction_list(self):
      return self.__transaction_list
    
class Credit_card:
   pin_number = 1234
   limit_money = 40000
   per_year = 150

   def __init__(self,card_no):
      self.__card_no = card_no
      self.__account_id = None

   @property
   def card_no(self):
      return self.__card_no

class Transaction:
   def __init__(self, type, money, balance, time, atm_id, account_id):
      self.__type = type
      self.__money = money
      self.__balance = balance
      self.__time = time
      self.__atm_id = atm_id
      self.__account_id = account_id
      self.__data = [type, balance, time, atm_id, account_id]
   
   @property
   def data(self):
      return self.__data

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
   

bank = Bank()

user1 = User('1-1101-12345-12-0','Harry Potter')
user2 = User('1-1101-12345-13-0','Hermione Jean Granger')
user_list = [user1,user2]

account1 = Account('1234567890',user1,20000)
account2 = Account('0987654321',user2,1000)
account_list = [account1,account2]

credit1 = Credit_card('12345')
credit2 = Credit_card('12346')
card_list = [credit1, credit2]

atm1 = ATM('1001')
atm2 = ATM('1002')


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

atm1.insert_card(account1,credit1,1234)
print("")

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

print("Hermione account before test :",account2.balance)
atm2.deposit(atm2,account2,1000)
print("Hermione account after test :",account2.balance)
# t1 = account2.transaction_list[0]
# print("Hermione Transaction : ",t1.type,":",t1.atm_id,"-",t1.money,"-",t1.balance)
for i in account2.transaction_list:
   if i == account2.transaction_list[0]:
      print("Hermione Transaction : ",i.type,":",i.atm_id,"-",i.money,"-",i.balance)
print("")

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

print(atm2.deposit(atm2,account2,-1))
print("")

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print("Hermione account before test :",account2.balance)
atm2.withdraw(atm2,account2,500)
print("Hermione account before test :",account2.balance)
# t2 = account2.transaction_list[1]
# print("Hermione Transaction : ",t2.type,":",t2.atm_id,"-",t2.money,"-",t2.balance)
for i in account2.transaction_list:
   if i == account2.transaction_list[1]:
      print("Hermione Transaction : ",i.type,":",i.atm_id,"-",i.money,"-",i.balance)
print("")

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print(atm2.withdraw(atm2,account2,2000))
print("")

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print("Harry account before test :",account1.balance)
print("Hermione account before test :",account2.balance)
atm2.transfer(atm2,account1,account2,10000)
print("Harry account after test :",account1.balance)
print("Hermione account after test :",account2.balance)
# t3 = account2.transaction_list[2]
# print("Hermione Transaction : ",t3.type,":",t3.atm_id,"-",t3.money,"-",t3.balance)
for i in account2.transaction_list:
   if i == account2.transaction_list[2]:
      print("Hermione Transaction : ",i.type,":",i.atm_id,"-",i.money,"-",i.balance)
      
print("")

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500

for i in account2.transaction_list:
   print("Hermioen Transaction : ",i.type,":",i.atm_id,"-",i.money,"-",i.balance)