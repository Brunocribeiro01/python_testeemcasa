#ano;mes;dia;glicemia;insulina;carb;kcal

linha = "Quinta;2012;ac;Normal;6;Abaixo;Acima;4;0;0;0;0;0;0;0;0;0;0;0;0;"


linha = linha.replace(" ",";")
linha = linha.replace("/",";")


vetor_linha = linha.split (";")

print (linha)


print (vetor_linha)