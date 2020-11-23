file=open('Desktop/Downloads/rosalind_ba6h.txt').read()
P=[[int(j) for j in i.split()] for i in file.split("\n")[0].lstrip("(").rstrip(")").replace("+","").split(")(")]


def ChromosomeToCycle(chromosome):
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


def ColoredEdges(P):
    edges=[]
    for chromosome in P:
        nodes=ChromosomeToCycle(chromosome)
        for j in range(len(chromosome)):
            edges.append((nodes[2*j],nodes[2*j+1]))
    return edges
    


print(ColoredEdges(P))
