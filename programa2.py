lista_glicemias = [107, 200, 63, 196, 154, 111, 164, 74, 77, 124, 133, 182, 77, 40, 102, 66, 165, 61, 105, 45, 71, 104, 148, 190, 179, 79, 96, 84, 169, 131]


for item in lista_glicemias:    
    if (item < 50):
        print(item, "Risco Abaixo")
    elif (item < 75):
        print(item, "Abaixo")
    elif (item < 140):
        print(item, "Normal")
    elif (item < 180):
        print(item, "Acima")
    else:
        print(item,"Risco Acima")

print(lista_glicemias)

soma = 0
for item in lista_glicemias:
    soma = soma + int(item)

media = soma / len(lista_glicemias)
print("A média de glicemia: ", media)


#para calcular a mediana é necessário ordenar a estrutura
lista_glicemias.sort()

indice_meio = int(len(lista_glicemias)/2)
print("A mediana de glicemia: ", lista_glicemias[indice_meio])

vezes_hipoglicemia = 0
for item in lista_glicemias:
    if int(item) < 70:
        #vezes_hipoglicemia = vezes_hipoglicemia + 1
        vezes_hipoglicemia += 1

print("Quantidade de vezes de hipoglicemia: ", vezes_hipoglicemia)

#len(lista_glicemias) --- 100%
#vezes_hipoglicemia   --- x
porcentagem_hipoglicemia = vezes_hipoglicemia * 100 / len(lista_glicemias)

print("Porcentagem de hipo: ", porcentagem_hipoglicemia)


valor_moda = ""
qtd_moda = 0
for item in lista_glicemias:
    ocorrencias = 0
    for outro_item in lista_glicemias:
        if (item == outro_item):
            ocorrencias += 1
    
    if (ocorrencias > qtd_moda):
        valor_moda = item
        qtd_moda = ocorrencias


print("A moda: ", valor_moda,"ocorrendo ", qtd_moda,"vezes")