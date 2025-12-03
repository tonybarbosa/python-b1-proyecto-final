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
    errores = False
    try:
        cashiers = CSVFileManager('./data/cashiers.csv').read()
        cajeros = CashierConverter().convert(cashiers)
    except:
        print("Error cargando cajeros, fichero no encontrado")
        errores = True

    try:
        customers = CSVFileManager('./data/customers.csv').read()
        clientes = CustomerConverter().convert(customers)
    except:
        print("Error cargando clientes, fichero no encontrado")
        errores = True

    try:
        drinks = CSVFileManager('./data/drinks.csv').read()
        bebidas = DrinkConverter().convert(drinks)
    except:
        print("Error cargando bebidaS, fichero no encontrado")
        errores = True
    
    try:
        sodas = CSVFileManager('./data/sodas.csv').read()
        gaseosas = SodaConverter().convert(sodas)
    except:
        print("Error cargando gaseosa, fichero no encontrado")
        errores = True

    try:
        hamburgers = CSVFileManager('./data/hamburgers.csv').read()
        hamburguesas = HamburgerConverter().convert(hamburgers)
    except:
        print("Error cargando hamburguesas, fichero no encontrado")
        errores = True

    try:
        happyMeals = CSVFileManager('./data/happyMeal.csv').read()
        comidasFelices = HappyMealConverter().convert(happyMeals)
    except:
        print("Error cargando happy meals, fichero no encontrado")
        errores = True

    # Fusionar las lista de cada producto en una sola lista
    if errores is True:
        return [], [], [], True
    
    productos = bebidas.copy()
    productos.extend(gaseosas)
    productos.extend(hamburguesas)
    productos.extend(comidasFelices)

    return cajeros, clientes, productos, errores