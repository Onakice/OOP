#| Example 1: Single Definition

print("Ex1")

x = 'global'
def f():
    def g():
        print(x)
    g()

f()

print("#####################################")

#| Example 2: Double Definition

print("Ex2")

x = 'global'
def f():
    x = 'enclosing'

    def g():
        print(x)
    g()

f()

print("#####################################")

#| Example 3: Triple Definition

print("Ex3")

x = 'global'
def f():
    x = 'enclosing'
    def g():
        x = 'local'
        print(x)
    g()

f()

print("#####################################")

#| Example 5: Local and Enclosing Name Space

print("Ex5")

def f():
    print('Start f()')
    def g():
        print('Start g()')
        print('End g()')
        return
    g()
    print('End f()')
    return

f()

print("#####################################")

#| Example 10: การอ้างถึงตัวแปร Global ภายใน function

print("Ex10")

counter = 0 # A global name

def update_counter():
    global counter # Declare counter as global
    counter = counter + 1 # Successfully update the counter

update_counter()
print(counter)
update_counter()
print(counter)
update_counter()
print(counter)

    # อีกวิธีหนึ่ง คือ ใช้ return แล้วให้ assignment ไปอยู่ที่ global scope
print("Another How to do about Return")

global_counter = 0

def update_global_counter(counter):
    return counter + 1  # Rely on a local name

global_counter = update_global_counter(global_counter)
print(global_counter)
global_counter = update_global_counter(global_counter)
print(global_counter)
global_counter = update_global_counter(global_counter)
print(global_counter)

print("#####################################")

#| Example 12: การสร้างตัวแปร Global จากภายใน function

print("Ex12")

def create_lazy_name():
    global lazy  # Create a global name, lazy
    lazy = 100
    return lazy

create_lazy_name()
print(lazy)  # The name is now available in the global scope

print("Ex12/2")

    # ในการอ้างถึงตัวแปรที่อยู่ใน enclosing scope จะใช้คำว่า nonlocal
# โดยจะหมายถึงตัวแปรที่อยู่ใน scope ถัดขึ้นไป

def func():
    var = 100  # A nonlocal variable
    def nested():
        nonlocal var  # Declare var as nonlocal
        var += 100
    nested()
    print(var)
func()

print("#####################################")

print("First Class Function")

def cube(n):
    return n*n*n

res = cube(5)
print(res)

my_cube = cube
res = my_cube(5)
print(res)

print("#####################################")

def cube2(n):
    return n*n*n

def my_map(method, argument_list):
    result = list()
    for item in argument_list:
        result.append(method(item))
    return result

my_list = my_map(cube, [1, 2, 3, 4, 5])
print(my_list)

print("#####################################")

def mutiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

a_list = [mutiply, subtract]
print(a_list[0](5, 5))
print(a_list[1](5, 5))

print("#####################################")

print("Lambda Function")

    # โครงสร้างของ Lambda Function มีดังนี้ lambda argument(s) : expresstion

x = lambda a : a + 10
print(x(5))

print('ตัวอย่างการใช้งาน')

def myfunc(n):
    return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))
print(tripler(11))

print('ตัวอย่างการใช้งาน กับ List Comprehension')

is_even_list = [lambda arg = x : arg * 10 for x in range(1, 5)]

for item in is_even_list:
    print(item())

print("#####################################")

#| Dictionary

print("Dictionary")

#  get vs [] for retrieving elements
my_dict = {'name' : 'Jack', 'age': 26}

#  Output : Jack
print(my_dict['name'])

#  Output : 26
print(my_dict.get('age'))

print(my_dict.get('address'))

                # print(my_dict['address'])

#   Changing and adding Dictionary Elements

#  Update value
my_dict['age'] = 27
print(my_dict)

#  add item
my_dict['address'] = 'Downtown'
print(my_dict)

#   Delete Dictionary

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
print(squares.pop(4))
print(squares)

# remove an arbitray item, return (key,value)
print(squares.popitem())
print(squares)

# remove all items
squares.clear()
print(squares)

# delete the dictionary itself
del squares
# print(squares)

# fromkeys()
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))
print(list(sorted(marks.values())))

print("#####################################")

