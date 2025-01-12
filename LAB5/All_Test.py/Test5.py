class Dog:

    def __init__(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 30:
            self.__age = new_age
        else:
            print("Please enter a valid age.")

    age = property(get_age, set_age)

my_dog = Dog(8)
print(f"Mydog is {my_dog.age} years old.")
print("One year later...")
my_dog.age += 1
print(f"My dog is now {my_dog.age} years old.")
#
my_dog.set_age(my_dog.get_age()+1)
print(f"My dog is now {my_dog.age} years old.")