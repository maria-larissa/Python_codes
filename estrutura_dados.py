            #SEQUÊNCIAS

#vetor/LISTA em python
#Consist em uma lista de valores que podem ser acessados e alterados
lista1=[1,2,3]
print("O tamanho da lista1 é {}".format(len(lista1)))
print(lista1)
lista2=[4,5,6,7]
print("O tamanho da lista2 é {}".format(len(lista2)))
print(lista2)

#concatenar os dois vetores
lista3=lista1+lista2
print("O tamanho da lista3 é {}".format(len(lista3)))
print(lista3)

#imprimir pedaços do verto/lista
print("lista ao contrário: {}".format(lista3[::-1]))         #imprimir lista ao contrário
print("ultimo valor: {}".format(lista3[-1]))           #imprimir lista ultimo valor         
print("2 ultimos valores: {}".format(lista3[-2:]))        #imprimir lista 2 ultimos valores
print("De 2 em 2: {}".format(lista3[0::2]))         #imprimir lista inteira de 2 em 2



#TUPLAS 
# São listas com valores imutáveis que podem ser de diferentes tipos
tupla1=(1,5,3)
print("tupla1: {}".format(tupla1))
tupla2=(5.6,"larissa",lista1)
print("tupla2: {}".format(tupla2))


#RANGES
#CORRIGIR!!!!
lista_ran1=range(1,50)
print("range1: {}".format(lista_ran1))
lista_ran2=range(-15,25)
print("range2: {}".format(lista_ran2))


                        #CONJUNTOS
# Nessa estrutura de dados não existe noção de ordem, ou seja, não há índices
#  e nem elementos repetidos
conj1={1,-5,8,9,9,10,-5}
print('conj1: {}'.format(conj1))
conj2={'z','a','c'}
print('conj2: {}'.format(conj2))
conj3={0,'b',5.7,'larissa'}
print('conj3: {}'.format(conj3))
conja={1,2,3,5}
print('conja: {}'.format(conja))
conjb={5,2,9,4}
print('conjb: {}'.format(conjb))
print("Interseção conjunto a e b: {}". format(conja & conjb));
print("União conjunto a e b: {}". format(conja | conjb));


                        #DICIONÁRIOS

