# Calcular o pi definindo número de iterações

# n = 2
# pi = 4.0
#
# numerador = -4
# denominador = 3
#
# for i in range(1, n):
#     pi += numerador / float(denominador)
#     numerador *= -1
#     denominador += 2
#     print(i, pi)


# Calculando pi definindo erro
# ERRO (estimativa) é o quanto eu estimo que o calculo vai estar errado, precisa ser maior que o erro verdadeiro

# TOLERÂNCIA é a margem em que o erro deve estar.


def calcula_pi(tolerancia):
    pi = 4.0
    pi_novo = pi
    erro = 2*tolerancia
    numerador = -4
    denominador = 3

    while erro > tolerancia:
        pi_novo = pi + numerador/float(denominador)
        erro = abs(pi_novo - pi)
        numerador *= -1
        denominador += 2
        pi = pi_novo

    return pi_novo, erro


tole = 1e-5
valor_pi, e = (calcula_pi(tole))
print("Pi = {}".format(valor_pi))
print("Erro = {}".format(e))
