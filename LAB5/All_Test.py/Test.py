class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.__year = year

my_car = Car("Porsche", "911 Carrera", 2020)

# print(my_car.year) # Can't be accessed
# print(my_car.__year) # Can't be accessed
# print(my_car.__year)
# print(my_car)

class Student:
    def __init__(self, stu_id, stu_name):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
    
    def get_id(self):
        return self.__stu_id

    def set_id(self, stu_id):
        if stu_id.isnumeric() and len(stu_id) == 8:
            self.__stu_id = stu_id
        else:
            raise ValueError("Invalid ID")
        
stu1 = Student('001', 'John')
stu2 = Student('002', 'Peter')
print(stu1.get_id())
stu1.set_id('66010100')
# stu1.set_id('6601020')
print(stu1.get_id())

