file = open('Desktop/Downloads/rosalind_ba3c (2).txt', 'r').read()
dnas=[i for i in file.split("\n") if i!='']

for i in range(len(dnas)):
    for j in range(len(dnas)):
        if dnas[i][1:]==dnas[j][:-1]:
            print(dnas[i]+" -> "+dnas[j])
