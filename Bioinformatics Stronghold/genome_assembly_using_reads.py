file= open('Desktop/Downloads/rosalind_gasm.txt').read()
strings=[i for i in file.split()]

def rev_comp(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1]) 

k=len(strings[0])-8 #k-mer(この値は、ある程度小さかったらなんでもいい)

totalstrings=[]
for string in strings:
    for i in range(0,len(string)-k+1):
        totalstrings.append(string[i:i+k])
        totalstrings.append(rev_comp(string[i:i+k]))       

    
d={}
#de Bruijin graph
for string in totalstrings:
    d[string[:-1]]=string[1:]


#cycle from graph
R=[]
root=list(d.keys())[1]
child=root
while True:
    R.append(child)
    child=d[child]
    if child ==root:
        break

genome=""
for r in R:
    genome +=r[0]
print(genome)
