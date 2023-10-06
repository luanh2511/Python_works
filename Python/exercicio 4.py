S= input ("Digite um numero inteiro: ")
if S.isnumeric():
    N = int(S)
    print ("o número digitado foi {0}".format (N))
else:
    print ("Erro: digite apenas números")
