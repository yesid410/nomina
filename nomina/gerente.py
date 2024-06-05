from rich import inspect
from colorama import Fore

from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombres, apellidos, salario):
        super().__init__(nombres, apellidos, "Gerente", salario)

    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.cargo})"

    def __repr__(self):
        return inspect.rich_repr(self)

    def mostrar_informacion(self):
        informacion = f"{self.nombres} {self.apellidos} {self.cargo}"
        return informacion
