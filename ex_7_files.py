f = open('r1.txt','r')

for file_line in f:
    print(file_line.strip('\n'))
