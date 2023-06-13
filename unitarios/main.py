import math
import unittest


def calculaequacao(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Primeira raiz: {} ".format(x1))
    print("Segunda raiz: {} ".format(x1))


a = float(input("Digite o valor para A: "))
b = float(input("Digite o valor para B: "))
c = float(input("Digite o valor para C: "))


calculaequacao(a, b, c)








