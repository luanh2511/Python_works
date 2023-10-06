import sqlite3
def ExibeDados(L):
    print("\nConsulta ao Banco de Dados")
    print("\Dados da tabela cadastro")
    print("-" * 35)
    print("{:7}{:20}{:>6}".format("Código""Nome","Idade"))
    print("-" * 18)
    for d in L:
        print("{:<7}{:20}{:>6}".format(d[0],d[1],d[2]))
        
    print("-" * 35)
    print("Encontrados {} registros ".format(len(dados)))

conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """
    insert into cadastro
    (codigo,nome,idade) values(?,?,?)
"""
print("Digite os dados separados por virgulas")
print("Codigo,Nome,idade")
Ler = input()
while Ler!="":
        D = Ler.split(",")
        try:
          cursor.execute(sql,D)
          conector.commit()

        except:
            print("{}Dados Invalidos".format(D))
        else:
            print(""*30,"Dados inseridos com sucesso")
        finally:
            print("Codigo,Nome,Idade")

        Ler = input()

sql = "select*from*cadastro"
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()
ExibeDados(dados)
print("\n\nFim do programa")
