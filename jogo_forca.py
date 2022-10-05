#variáveis
pal_secreta='goiaba'
acertou=False
enforcou=False
erros=0

#lista / vetor
acertos=['_','_','_','_','_','_']
letras_erradas=[]

#tamanho da string
#len(pal_secreta)

#looping
while(not acertou and not enforcou):
    #Verifica quantidade de erros
    if(erros <= len(pal_secreta)):
        print("")
        chances=len(pal_secreta)-erros
        print("Número de chances: {}".format(chances))
        #recebe a letra do chute
        print("")
        chute=input("Digite uma letra: ")

        #confere se letra está na palavra secreta
        if (chute in pal_secreta):
            pos=0

            #coloca letra na posição certa
            for letra in pal_secreta:
                if(letra == chute):
                    acertos[pos]=letra
                pos+=1

        #se não estiver incrementa o erro        
        else:
            letras_erradas.append(chute)
            erros+=1

        #caso tenha acertado a palavra
        if('_' not in acertos):
            acertou=True

    #se atingiu limite de quantidade de erros        
    else:
        enforcou=True

    print("")
    print(acertos)
    print("")
    print("Letras erradas: ", end="")
    i=0
    for i in range(0,len(letras_erradas)):
        print(letras_erradas[i], end=" ")
        i+=1
    print("")
    #print("Letras erradas: {}".format(letras_erradas))
    #outra formas de printar menssagens junto com variaveis/arrays.
    #print("Letras erradas: {}" + str(letras_erradas))
    

if(enforcou):
    print("GAME OVER!")
if(acertou):
    print("CONGRATULATIONS!")
    