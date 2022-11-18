
from sympy import Symbol, solve, exp, cos

matricula = 239
c = matricula % 10

e = 2.718281828459

def func1(x):
    return e**(x-2) + e**(x-3)+ e**(x) - 5*(c + 1)
    #return exp(x-2) + exp(x-4) + exp(x) - 5*(c + 1)


def func2(x):
    return 3*x**3 - 2*x**2 - 5*x - 4*c


def func3(x):
    return 2 * cos(4*(c+1)*x) + 5


x = Symbol('x')

result = solve(func1(x))
print('Primeira equação: ')
print(result)
print('\n')

result = solve(func2(x))
print('Segunda equação: ')
print(result)

result = solve(func3(x))
print('\n')
print('Terceira equação: ')
print(result)
print('\n')