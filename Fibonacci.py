print("Fibo")
numero_termos = int(input("Entre com o numero de termos:"))
a = 0
b = 1
print(a, end = ',')
print(b, end = ',')
i = 1
while i <= numero_termos - 2:
    #print(i, palavra)
    c = a + b
    print(c, end=',')
    # a = b
    # b = c
    a, b = b, c
    i = i + 1
