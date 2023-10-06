import os
os.getcwd ()
os.chdir ('C:\\Users\luanh\OneDrive\Documentos\CEUNSP\Python')
os.getcwd ()

try:
    data = open ('sketch.txt')
    #print (data.readline(),end = ' ')
    #print (data.readline(), end = ' ')


#data.seek(0)

#for each_line in data:
    #print(each_line, end = ' ')

    #data.close()

#data = open('sketch.txt')
    
    for each_line in data:
        #if not each_line.find(':') == -1:
        try:
            (role, line_spoken) = each_line.split (':',1)
            print (role, end = ' ')
            print('said: ', end = ' ')
            print(line_spoken, end = ' ')
        except:
            pass
        data.close()
except:
        print(' O arquivo de dados não esta na pasta')
