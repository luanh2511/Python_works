man = []
other = []

try:

    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken)=each_line.split(':',1)
            line_spoken=line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('O arquivo de dados não esta na pasta')

try:
    with open('man_data.txt','w')as man_file:
        print(man, file = man_file)
    with open('other_data.txt','w')as other_file:
        print(other, file = other_file)
        
    #man_file=open('man_data.txt','w')
    #other_file=open('other_data.txt','w')

    #man_file.close()
    #other_file.close()
        
except IOError:
    print('File error')

