list = (12,2,4,8,29,45,78,36,-17,2,12,8,3,3,-52)
list_pares = []
soma_neg = 0
media = 0
soma = 0

for i in range(0, len(list)):
    soma = soma + list[i]

    #cria lista só com os números pares
    if list[i] % 2 == 0:
        list_pares.append(list[i])
    
    #soma números negativos
    if list[i] < 0:
        soma_neg = soma_neg + list[i]

    #defini valores iniciais para max e min e cria contador para 1º elemento.
    if i == 0:
        cont = 1
        max_value = list[i]
        min_value = list[i]
    
    #atualiza valores max, min e cont.
    else:
        if list[i] == list[0]:
            cont = cont+1
        if list[i] > max_value:
            max_value = list[i]
        if list[i] < min_value:
            min_value = list[i]
    
    #calcula média
    if i == (len(list)-1):
        media = (float)(soma/(len(list)))
    
    
print("a - O maior elemento da lista é {}.".format(max_value))
print("b - O menor elemento da lista é {}.".format(min_value))
print("c - Os elementos pares da lista são {}.".format(list_pares))
print("d - O 1º elementos da lista aperce na lista {} vezes.".format(cont))
print("e - A média dos elementos da lista é {:.2f}.".format(media))
print("f - A soma dos elementos negativos da lista é {}.".format(soma_neg))