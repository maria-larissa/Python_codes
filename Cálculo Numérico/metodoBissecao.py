# Método Bisseção para determinar raízes de funções não lineares

# inicializa as iterações
# verificar em qual subintervalo a função muda de sinal
# Calcula o no intervalo
#
import math as math


def funcao(x):
    # return math.exp(x) - 5 * x
    return x**3 - 9*x + 3


def met_bissecao(a, b, epsilon, n_max_iteracao):
    # vamos buscar o zero da função no tam_intervalo [a, b]
    # retorna um tupla boolean houverro, double raiz
    fa = funcao(a)
    print("f(a) = ", fa)
    fb = funcao(b)
    print("f(a) = ", fb)

    if (fa * fb) > 0:
        print("ERRO! A função não muda de sinal")
        return (True, None)

    else:
        print("k\t\t a \t\t\t\t\t f(a) \t\t\t\t b \t\t\t\t\t f(b)"
              " \t\t\t\t x \t\t\t\t\t f(x) \t\t\t tamanho do intervalo")

        tam_intervalo = abs(b - a)  # armazena tamnho do intervalo (PRECISÃO)
        x = (a + b) / 2  # Armazena valor medio do intervalo
        fx = funcao(x)  # calcula e armazena valor f(x)
        print("0\t %e\t\t %e\t\t %e\t\t %e\t\t %e\t\t %e\t\t\t\t %e" % (a, fa, b, fb, x, fx, tam_intervalo))

        # testar se a precição foi atingida da primeira vez
        if tam_intervalo <= epsilon:
            return (False, x)

        # se a precisão não foi atingida, atualiza e repete o processo
        k = 1

        while k <= n_max_iteracao:

            if (fa * fx) > 0:
                a = x
                fa = fx
            else:
                b = x
                fb = fx

            tam_intervalo = abs(b - a)  # armazena tamnho do intervalo (PRECISÃO)
            x = (a + b) / 2  # Armazena valor medio do intervalo
            fx = funcao(x)  # calcula e armazena valor f(x)


             # print("%d\t %.2f\t\t %.6f\t\t %.2f\t\t %.6f\t\t %.2f\t\t %.6f\t\t\t\t %.2f" % (k, a, fa, b, fb, x, fx, tam_intervalo))

            print("%d\t %e\t\t %e\t\t %e\t\t %e\t\t %e\t\t %e\t\t\t\t %e" % (k, a, fa, b, fb, x, fx, tam_intervalo))

            # testar se a precição foi atingida apoś a tualização de valores
            if tam_intervalo <= epsilon:
                return (False, x)

            k = k + 1

        print("Erro! numero máximo de iterações atingido.")
        return (False, None)


x1 = 0
x2 = 1
precisao = 0.001
max_itera = 20
(houve_erro, raiz) = (met_bissecao(x1, x2, precisao, max_itera))

if houve_erro:
    print("Houve um erro no método da Bisseção")
else:
    print("O valor da raiz que existe no intervalo [%e, %e] é %s" % (x1, x2, raiz))
