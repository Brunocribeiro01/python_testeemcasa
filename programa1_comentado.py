#ano;glicemia;insulina;carb;kcal

linha = "2024;146;20 0;20"

#O método replace é usado para substituir partes de uma string por outra coisa. Aqui, ele está sendo 
#usado para substituir o espaço (" ") por um ponto e vírgula (";"). Isso faz com que todos os 
#separadores dos dados sejam consistentes, utilizando ponto e vírgula.

linha = linha.replace(" ",";")



#Este código usa o método split para dividir a string armazenada na variável linha em partes 
#separadas sempre que encontra um ponto e vírgula (;).

vetor_linha = linha.split (";")

#Este comando imprime o conteúdo atual da variável linha. Continuando com o nosso exemplo, 
#ele imprimirá "2024;146;20;0;20".

print (linha)

#Este comando imprime a lista que foi criada pelo método split. Usando o nosso exemplo 
#anterior, ele imprimirá  ['2024', '146', '20', '0', '20'].
print (vetor_linha)