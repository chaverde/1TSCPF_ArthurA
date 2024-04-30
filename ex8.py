# ex8
ano = int(input("Ano: "))
if ano >= 1000 and ano <= 2999:
    if (ano % 4) == 0 and (ano % 100) != 0:
        print("Ano bissexto")
    else:
        print("Ano não é bissexto")
else:
    print("Ano inválido!")
