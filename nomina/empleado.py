from rich import inspect
from colorama import Fore

class Empleado:
    def __init__(self, nombres, apellidos, cargo, salario):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.cargo})"

    def __repr__(self):
        return inspect.rich_repr(self)

    def mostrar_informacion(self):
        informacion = f"{self.nombres} {self.apellidos} {self.cargo}"
        return informacion

