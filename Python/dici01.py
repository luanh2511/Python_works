pecas={}
print ("'Leitura dos dados")
while True:
    cod = int(input(" Digite o código: "))
    if cod == 0:
        break
    elif cod in pecas:
        print ("A peca {} já existe no cadastro" .format (cod))
        continue
    qtde = int(input("Digite a quantidade: "))
    pecas[cod] = qtde
    
print ("Fim da leitura dos dados\n")

print ("Estoque de peças")

for c in pecas:
    print (" {1:4} unidades da peça {0}".format (c, pecas[c]))
print ("\nFIM DO PROGRAMA")
