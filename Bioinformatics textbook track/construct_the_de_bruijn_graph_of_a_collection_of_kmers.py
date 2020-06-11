file = open('Desktop/Downloads/rosalind_ba3e.txt', 'r').read()
paptterns=[i for i in file.split("\n") if i!='']


def DeBruijn(patterns):
    d={}
    for i in range(len(patterns)):
        if patterns[i][:-1] in  d.keys():
            d[patterns[i][:-1]].append(patterns[i][1:])
        else:
            d[patterns[i][:-1]]=[patterns[i][1:]]
        
    for edge in d:
        print(edge+" -> " +','.join(d[edge]))

DeBruijn(paptterns)
