import pandas as pd
from util.converter import CashierConverter, \
                           CustomerConverter, \
                           DrinkConverter, \
                           SodaConverter, \
                           HamburgerConverter, \
                           HappyMealConverter

'''
from users.user import *
from products.product import *
'''


class CSVFileManager:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> str:
        return pd.read_csv(self.path)

    def write(self, dataFrame):
        pass


def cargar_datos():
    cashiers = CSVFileManager('./data/cashiers.csv').read()
    cajeros = CashierConverter().convert(cashiers)

    customers = CSVFileManager('./data/customers.csv').read()
    clientes = CustomerConverter().convert(customers)

    drinks = CSVFileManager('./data/drinks.csv').read()
    bebidas = DrinkConverter().convert(drinks)

    sodas = CSVFileManager('./data/sodas.csv').read()
    gaseosas = SodaConverter().convert(sodas)

    hamburgers = CSVFileManager('./data/hamburgers.csv').read()
    hamburguesas = HamburgerConverter().convert(hamburgers)

    happyMeals = CSVFileManager('./data/happyMeal.csv').read()
    comidasFelices = HappyMealConverter().convert(happyMeals)

    # Fusionar las lista de cada producto en una sola lista

    productos = bebidas.copy()
    productos.extend(gaseosas)
    productos.extend(hamburguesas)
    productos.extend(comidasFelices)

    return cajeros, clientes, productos