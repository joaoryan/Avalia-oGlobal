from sympy import Symbol, solve

matricula = 239
c = matricula % 10


def V1():
    return 10 + (2 * c)


def V2():
    return 5 + (2 * c)


def malhaEsquerda(I1, I2):
    return -V1() + 20 * I1 + 25 * (I1 - I2)


def malhaDireita(I2, I3):
    return -V2() + 25 * I3 + 10 * (I3 - I2)


def leiDosNos(I1, I2, I3):
    return I1 + I2 + I3


I1 = Symbol('I1')
I2 = Symbol('I2')
I3 = Symbol('I3')

f = malhaEsquerda(I1, I2)
g = malhaDireita(I2, I3)
h = leiDosNos(I1, I2, I3)

resultado = solve((f, g, h))

print('\n' * 100)

for corrente in resultado:
    print(str(corrente) + ' -> ' + str(resultado[corrente]) + 'A')

