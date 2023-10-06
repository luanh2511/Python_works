print("Inicio do programa")
arqreais = open("Valores_Reais.txt","w")
x=float(input("Digite um numero real: "))
while x!=0:
    arqreais.write("{0:3f}\n".format(x))
    x=float(input("Digite um numero real: "))
arqreais.close()
print("Fim do programa")
