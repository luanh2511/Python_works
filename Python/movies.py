movies = ["Exterminador do Futuro",1985, "Arnold Schwazenegger",["Rambo",1982,"Sylvester Stallone",["Star Wars",1977,"Luke Skywalker / Mark Hamill",["Tropa de Elite",2007,"Wagner Moura"]]]]
for each_flick in movies:
    print (each_flick)

for each_item in movies:
    if isinstance (each_item,list):
        for nested_item in each_item:
            if isinstance (nested_item, list):
                for deeper_item in nested_item:
                    print (deeper_item)
        else:
                print(nested_item)
    else:
            print(each_item)
        
