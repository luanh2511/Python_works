entrada = input("Digite um numero de O a 100: ")
numero = int(entrada)

if not 0 < numero < 100:
    print ("O numero digitado é invalido.")
    
if numero % 2 == 0:
    print ("O numero digitado é par.")
    
if numero % 2 != 0:
    print ("O numero digitado é impar.") 
