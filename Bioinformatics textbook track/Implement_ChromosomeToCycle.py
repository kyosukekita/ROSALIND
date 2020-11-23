file=open('Desktop/Downloads/rosalind_ba6f.txt').read()
chromosome=[int(i) for i in file.strip("()").split()]


def chromosomeToCycle(chromosome):
    nodes=[0 for _ in range(2*len(chromosome))]
    for j in range(0,len(chromosome)):
        i=chromosome[j]
        if i>0:
            nodes[2*j-1]=2*i-1
            nodes[2*j]=2*i
        else:
            nodes[2*j-1]=-2*i
            nodes[2*j]=-2*i-1
    
    return nodes
            
print("("+' '.join(map(str,chromosomeToCycle(chromosome)))+")")
