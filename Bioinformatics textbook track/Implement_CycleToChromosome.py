file=open('Desktop/Downloads/rosalind_ba6g.txt').read()
nodes=[int(i) for i in file.strip("()").split()]


def CycleToChromosome(nodes):
    chromosome=[0 for _ in range(len(nodes)//2)]
    for j in range(len(nodes)//2):
        if nodes[2*j]<nodes[2*j+1]:#添え字注意。問題文は1からスタートだけど、、、
            chromosome[j]=(nodes[2*j+1]//2)
        else:
            chromosome[j]=(-nodes[2*j]//2)
    
    return chromosome


def plus(perm):
    tmp=[]
    for i in perm:
        if i>0:
            tmp.append("+"+str(i))
        else:
            tmp.append(str(i))
    return tmp
            
print("("+' '.join(plus(CycleToChromosome(nodes)))+")")
