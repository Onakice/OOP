from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
import os

import uvicorn

app = FastAPI()
static_directory = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_directory, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_directory), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=[""],
)

class User:
    def __init__(self, name : str, id:str) -> None:
        self.__name = name
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def id(self) -> str:
        return self.__id
    
class Account :
    def __init__ (self, user: User, password: str) -> None:
        self.__user = user
        self.__password = password
        self.__address = ''
        self.__transaction_list = []
    
    @property
    def user(self) -> User:
        return self.__user
    
    @property
    def password(self) -> str:
        return self.__password
    
    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def transaction_list(self) -> list:
        return self.__transaction_list
    
    def add_address(self, address: str) -> None:
        self.__address = address

class Customer_account(Account):
    def __init__(self, user: User, password: str) -> None:
        super().__init__(user, password)
        self.__basket = []
        self.__success_order = []
        self.__unsuccess_order = []
        self.__coupon_list = []

    @property
    def basket(self) -> list:
        return self.__basket
     
    @property
    def success_order(self) -> list:
        return self.__success_order
    
    @property
    def unsuccess_order(self) -> list:
        return self.__unsuccess_order
    
    @property
    def coupon_list(self) -> list:
        return self.__coupon_list

class Shop_account(Account) :
    def __init__(self, user: User, password: str) -> None:
        super().__init__(user, password)
        self.__branch = []
    
    @property
    def branch(self) -> list:
        return self.__branch
    
    def update_order_status(self, order_id: str, status: str) -> None:
        pass

class Status:
    def __init__(self, status: str, date: str) -> None:
        self.__status = status
        self.__date = date
    
    @property
    def status(self) -> str:
        return self.__status
    
    @property
    def date(self) -> str:
        return self.__date

class Pizza :
    def __init__(self, name: str, price: int) -> None:
        self.__face = name
        self.__price = price
    
    @property
    def face(self) -> str:
        return self.__face
    
    @property
    def price(self) -> int:
        return self.__price
    
class Pizza_item :
    def __init__(self, pizza: Pizza, size : str, quantity: int) -> None:
        self.__pizza = pizza
        self.__size = size
        self.__quantity = quantity
        
    @property
    def pizza(self) -> Pizza:
        return self.__pizza
    
    @property
    def size(self) -> str:
        return self.__size
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
class Drink:
    def __init__(self):
        self.__drink_type = []
        self.__size = []
    
    @property
    def drink_type(self):
        return self.__drink_type
    
    @property
    def size(self):
        return self.__size

class Drink_item:
    def __init__(self, drink: Drink, size: str, quantity: int) -> None:
        self.__drink = drink
        self.__size = size
        self.__quantity = quantity
    
    @property
    def drink(self) -> Drink:
        return self.__drink
    
    @property
    def size(self) -> str:
        return self.__size
    
    @property
    def quantity(self) -> int:
        return self.__quantity  
    
class Combo:
    def __init__(self, pizza: Pizza, drink: Drink) -> None:
        self.__pizza = pizza
        self.__drink = drink
    
    @property
    def pizza(self) -> Pizza:
        return self.__pizza
    
    @property
    def drink(self) -> Drink:
        return self.__drink
    
    def add_pizza(self, pizza: Pizza) -> None:
        pass

    def add_drink(self, drink: Drink) -> None:
        pass

class Basket :
    def __init__(self, user : User) -> None:
        self.__owner = user
        self.__pizza_list = []

    @property
    def owner(self) -> User:
        return self.__owner
    
    @property
    def pizza_list(self) -> list:
        return self.__pizza_list

    def add_pizza(self, pizza: Pizza_item) -> None:
        self.__pizza_list.append(pizza)

    def remove_pizza(self, pizza: Pizza_item) -> None:
        self.__pizza_list.remove(pizza)

    def get_total_price(self) -> int:
        total_price = 0
        for pizza in self.__pizza_list:
            if pizza.size == "S":
                pizza_price = pizza.pizza.price * pizza.quantity
            elif pizza.size == "M":
                pizza_price = (pizza.pizza.price + 30)* pizza.quantity 
            elif pizza.size == "L":
                pizza_price = (pizza.pizza.price + 50)* pizza.quantity
            total_price += pizza_price
        return total_price

#Ice shop
class Shop:
    def __init__(self, shop_id_branch: int) -> None:
        self.__shop_id_branch = shop_id_branch
        self.__shop_stock = []
    
    @property
    def shop_id_branch(self):
        return self.__shop_id_branch
    
    @property
    def shop_stock(self):
        return self.__shop_stockt

    def add_stock(self, stock: list) -> None:
        self.__shop_stock.append(stock)

    def get_stock():
        pass

    def check_stock():
        pass

class Shop_account(Account) :
    def __init__(self, user: User, password: str) -> None:
        super().__init__(user, password)
        self.__branch = []
    
    @property
    def branch(self) -> list:
        return self.__branch
    
    def update_order_status(self, order_id: str, status: str) -> None:
        pass

class Shop_stock(Shop):
    def __init__(self):
        Shop.__init__(self)
        self.__pizza_list_amount = []
        self.__drink_list_amount = []

    @property
    def pizza_list_amount(self):
        return self.__pizza_list_amount
    
    @property
    def drink_list_amount(self):
        return self.__drink_list_amount


class Coupon:
    def __init__(self, code: str, discount: int, date_avaible: str) -> None:
        self.__code = code
        self.__discount = discount
        self.__date_avaible = date_avaible
    
    @property
    def code(self) -> str:
        return self.__code
    
    @property
    def discount(self) -> int:
        return self.__discount

    @property
    def date_avaible(self) -> str:
        return self.__date_avaible


class Controller :
    def __init__(self) -> None:
        self.__user_list = []
        self.__shop_list = []

    @property
    def user_list(self) -> list:
        return self.__user_list
    
    @property
    def shop_list(self) -> list:
        return self.__shop_list

    def add_user(self, name: str, id: str) -> None:
        self.__user_list.append(User(name, id))

    def add_shop(self, shop_id_branch: int) -> None:
        self.__shop_list.append(Shop(shop_id_branch))

    def search_user_by_id(self, user_id: str) -> User:
        for user in self.__user_list:
            if user.id == user_id:
                return user
        return None 
    
    def check_stock(self, shop_id_branch: int) -> str:
        for shop in self.shop_list:
            if shop.shop_id_branch == shop_id_branch:
                return shop.shop_stock()
        

controller = Controller()
controller.add_user('tur', "123")
shop1 = controller.add_shop(101)
shop2 = controller.add_shop(102)
# shop1.add_stock("pepperoni", "margherita", "hawaiian", "mushroom", "cheese", "tomato")
# shop2.add_stock("pepperoni", "seafood","cheese", "pineapple")
baskettest = Basket(controller.search_user_by_id("123"))

pizzatest1 = Pizza("pepperoni", 10)
pizzatest2 = Pizza("margherita", 9)

pizzatest1_item = Pizza_item(pizzatest1, "S", 2)
pizzatest2_item = Pizza_item(pizzatest2, "L", 1)

baskettest.add_pizza(pizzatest1_item)
baskettest.add_pizza(pizzatest2_item)
print(baskettest.get_total_price())

@app.post('/user', tags=["User"])
def create_user(name: str, id: str):
    controller.add_user(name, id)
    return {"message": "user created"}

@app.get ('/user/{user_id}', tags=["User"])
def read_user(user_id: str):
    user = controller.search_user_by_id(user_id)
    if user:
        return {"name": user.name, "id": user.id}
    else:
        return {"message": "user not found"}


    
@app.post('/basket/{user_id}', tags=["Basket"])
def add_to_basket(user_id: str, face: str, price: int, size: str, quantity: int) -> dict:
    user = controller.search_user_by_id(user_id)
    if user:
        basket = Basket(user)
        basket.add_pizza(Pizza_item(Pizza(face, price), size, quantity))
        return {"message": "pizza added to basket",
                'pizza_list' : basket.pizza_list.pizza_face}
    else:
        return {"message": "user not found"}
    
@app.get('/basket/{user_id}', tags=["Basket"])
def get_basket(user_id: str):
    user = controller.search_user_by_id(user_id)
    if user:
        basket = Basket(user)
        return {'message' : basket.get_total_price(),
                'basket' : basket.pizza_list}
    else:
        return {"message": "user not found"}

@app.get('/shop', tags=["Search Shop List"])
def get_shop():
    shop_info = []
    for shop in controller.shop_list:
        shop_info.append({"shop_id_branch": shop.shop_id_branch})
    return {"Shops list": shop_info}
# """ 
@app.post('/shop', tags=["Check Shop Stock"])
def check_shop_stock(shop_id_branch: int):
    shop = controller.check_stock(shop_id_branch)
    if shop:
        return {"shop_id_branch": shop.shop_id_branch, "stock": shop.shop_stock}
    else:
        return {"message": "shop not found"}

# """
    
print("Server ON!!!")