from sympy import Integral, Symbol

matricula = 239
c = matricula % 10

def minha_funcao(x):
    return (1 / x**(1/3)) - x**5 - 6*x - 2 * c

x = Symbol('x')


area_sob_curva = Integral(minha_funcao(x), (x, 3, 6)).doit()

print(area_sob_curva)
