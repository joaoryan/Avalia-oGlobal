
from sympy import Symbol, solve, exp, cos

matricula = 239
c = matricula % 10


def func1(x):
    return exp(x-2) + exp(x-4) + exp(x)


def func2(x):
    return 3*x**3 - 2*x**2 - 5*x


def func3(x):
    return 2 * cos(4*(c+1)*x)


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