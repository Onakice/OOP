class Dog:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 30:
            self.__age = new_age
        else:
            print("Please enter a valid age.")

my_dog = Dog(9)
print(my_dog.age)
my_dog.age = 10
print(my_dog.age)
my_dog.age += 10
print(my_dog.age)
# my_dog.age += 10
# print(my_dog.age)         # Please enter a valid age