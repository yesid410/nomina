from rich import inspect, table, console
from colorama import Fore

from empleado import Empleado
from gerente import Gerente

class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def nombrar_gerente(self, gerente):
        self.gerente = gerente

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_empleados(self, datos):
        for dato in datos:
            nombres, apellidos, cargo, salario = dato
            empleado = Empleado(nombres, apellidos, cargo, salario)
            self.agregar_empleado(empleado)

    def calcular_nomina(self):
        nomina_departamento = 0
        for empleado in self.empleados:
            nomina_departamento += empleado.salario
        return nomina_departamento + self.gerente.calcular_salario()

    def mostrar(self):
        console1 = console.Console()
        console1.print(f"[bold yellow]- {self.nombre}[/bold yellow]: [bold green]$ {self.calcular_nomina():,}[/bold green]")
