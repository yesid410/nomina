from rich import inspect, console
from colorama import Fore

from departamento import Departamento

class Empresa:
    def __init__(self, nombre, departamentos):
        self.nombre = nombre
        self.departamentos = departamentos

    def calcular_nomina(self):
        nomina_total = 0
        for departamento in self.departamentos:
            nomina_total += departamento.calcular_nomina()
        return nomina_total

    def mostrar(self):
        console1 = console.Console()

        console1.print(f"[bold red]{self.nombre}[/bold red]")
        console1.print("----------------")
        for departamento in self.departamentos:
            departamento.mostrar()
        console1.print(f"[bold green]                            $ {self.calcular_nomina():,}[/bold green]")

