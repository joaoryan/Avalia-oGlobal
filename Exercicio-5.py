
from sympy import Symbol, solve, sin, exp

matricula = 9594
c = matricula % 10


def func1(x):
    return exp(x-3) + exp(x-1) + exp(x) - 1 - c


def func2(x):
    return x**4- 4*x**3 + 3*x - c


def func3(x):
    return 4 * sin(x*(c+1)) + 2


x = Symbol('x')

result = solve(func1(x))
print('Primeira equação: ')
print(result)
print('\n' * 2)

result = solve(func2(x))
print('Segunda equação: ')
print(result)

result = solve(func3(x))
print('\n' * 2)
print('Terceira equação: ')
print(result)
