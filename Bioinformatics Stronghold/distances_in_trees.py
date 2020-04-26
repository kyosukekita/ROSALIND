from Bio import Phylo
from io import StringIO

def nwck(filename):
    f=open(filename).read()
    data=[a for a in f.split("\n") if a!='']
    
    answer=[]
    for i in range(0,len(data),2):
        tree=Phylo.read(StringIO(data[i]),"newick") #To use string as input or output instead of actual files, use StringIO
        x,y=data[i+1].split()
        
        clades=tree.find_clades()
        for clade in clades:
            clade.branch_length=1
            
        answer.append(tree.distance(x,y))
        
    print(*answer)
            
nwck('Desktop/Downloads/rosalind_nwck.txt') 
