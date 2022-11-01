from sympy import Limit, Symbol, S

matricula = 9594
c = matricula % 10


def minha_funcao(x):
    return ((2*x**4 - 2) / (5 - 5*x**2)) * (c + 4)

x = Symbol('x')

# x -> 1
resultado_1 = Limit(minha_funcao(x), x, 1).doit()

# x -> oo
resultado_2 = Limit(minha_funcao(x), x, S.Infinity).doit()

# x -> -oo
resultado_3 = Limit(minha_funcao(x), x, -S.Infinity).doit()

print('Resultado para x -> 1: ' + str(resultado_1))
print('Resultado para x -> oo: ' + str(resultado_2))
print('Resultado para x -> -oo: ' + str(resultado_3))