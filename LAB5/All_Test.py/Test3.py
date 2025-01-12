class Pizza:

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self
    
    def display_toppings(self):
        print("This Pizza has : ")
        for topping in self.toppings:
            print(topping.capitalize())



Pizza.add_topping("mushrooms") \
    # .add_topping("olives") \
    # .add_topping("chicken") \
    # .display_toppings()

Pizza.display_toppings()