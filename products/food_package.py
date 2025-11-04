# Write your code here
# Se importa la clase ABC y abstractmethod

from abc import ABC, abstractmethod


class FoodPackage (ABC):

    @abstractmethod
    def pack(self) -> str:   # clase abstracta
        pass

    @abstractmethod
    def material(self) -> str:   # clase abstracta
        pass

    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"

# Se crean las clases que heredan de los metodos abstractos de FoodPackage


class Wrapping(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Food Wrap Paper"

    def material(self) -> str:
        return "Paper"


class Bottle(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Bottle"

    def material(self) -> str:
        return "Plastic"


class Glass(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Glass"

    def material(self) -> str:
        return "Glass"


class Box(FoodPackage):
    # Write your code here
    def pack(self) -> str:
        return "Box"

    def material(self) -> str:
        return "Cardboard"
