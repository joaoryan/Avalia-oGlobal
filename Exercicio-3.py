from sympy import Integral, Symbol

matricula = 9594
c = matricula % 10


def minha_funcao(x):
    return x**3 - 4*x**2 + 5*x - c

x = Symbol('x')


area_sob_curva = Integral(minha_funcao(x), (x, 0.0, 5.0)).doit()

print(area_sob_curva)


