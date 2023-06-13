from main import *
import unittest


print(calculaequacao(1, 20, -4))

class TestClass(unittest.testCase):
    def testemetodo(self):
        response = calculaequacao(1, 20, -4)
        self.assertEqual(0.2, response.x_linha, "falhou")

