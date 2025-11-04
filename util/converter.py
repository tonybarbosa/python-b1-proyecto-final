from abc import ABC, abstractmethod
# Write your code here
from users.user import Cashier, Customer
from products.product import Drink, Soda, Hamburger, HappyMeal


class Converter(ABC):
    @abstractmethod
    def convert(self, dataFrame, *args) -> list:
        pass

    def print(self, objects):
        for item in objects:
            print(item.describe())


class CashierConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        cajeros = [Cashier(row['dni'], row['name'], row['age'],
                           row['timetable'], row['salary'])
                   for _, row in dataFrame.iterrows()]
        return cajeros


class CustomerConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        clientes = [Customer(row['dni'], row['name'], row['age'],
                             row['email'], row['postalcode'])
                    for _, row in dataFrame.iterrows()]
        return clientes


class DrinkConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        productos = [Drink(row["id"], row['name'], row['price'])
                     for _, row in dataFrame.iterrows()]
        return productos


class SodaConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        productos = [Soda(row["id"], row['name'], row['price'])
                     for _, row in dataFrame.iterrows()]
        return productos


class HamburgerConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        productos = [Hamburger(row["id"], row['name'], row['price'])
                     for _, row in dataFrame.iterrows()]
        return productos


class HappyMealConverter(Converter):
    # Write your code here
    def convert(self, dataFrame):
        productos = [HappyMeal(row["id"], row['name'], row['price'])
                     for _, row in dataFrame.iterrows()]
        return productos
