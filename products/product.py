from abc import ABC, abstractmethod
# Write your code here
from products.food_package import FoodPackage, Wrapping, Glass, Bottle, Box


class Product(ABC):
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    # se deja la linea intencionadamente larga (fuera de PEP8),
    # evitar espacios en blanco indeseados en la impresion
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."

    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def foodPackage(self) -> FoodPackage:
        pass


class Hamburger(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Hamburguer"

    def foodPackage(self) -> FoodPackage:
        return Wrapping()


class Soda(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Soda"

    def foodPackage(self) -> FoodPackage:
        return Glass()


class Drink(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "Drink"

    def foodPackage(self) -> FoodPackage:
        return Bottle()


class HappyMeal(Product):
    # Write your code here
    def __init__(self, id: str, name: str, price: float):
        super().__init__(id, name, price)

    def type(self) -> str:
        return "HappyMeal"

    def foodPackage(self) -> FoodPackage:
        return Box()
