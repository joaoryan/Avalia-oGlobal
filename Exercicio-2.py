from sympy import Symbol, Derivative

matricula = 239
c = matricula % 10

def eqPosicao(t):
    return (t ** (1/4)) + (1/t**2) -3 * c


t = Symbol('t')
eqVelocidade = Derivative(eqPosicao(t), t).doit()

print('\nv(t) = ', eqVelocidade, '\n')

velocidade_3 = Derivative(eqPosicao(t), t).doit().subs({t: 7})

print('\nv(3) = ', velocidade_3, '\n')

eqAceleracao = Derivative(eqVelocidade, t).doit()

print('\na(t) = ', eqAceleracao, '\n')

aceleracao_5 = Derivative(eqVelocidade, t).doit().subs({t: 2})

print('\na(5) = ', aceleracao_5, '\n')
