import unittest

from empresa import Empresa
from departamento import Departamento
from gerente import Gerente
from empleado import Empleado

class TestEmpresa(unittest.TestCase):

    def test_depto_calcular_nomina(self):
        dpto = Departamento('A', Gerente('gA', 'gA', 100))
        self.assertEqual(dpto.calcular_nomina(), 102, "Incorrecto! nomina departamento")


if __name__ == '__main__':
    unittest.main()        