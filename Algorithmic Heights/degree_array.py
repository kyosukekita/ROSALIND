edges= open('Desktop/Downloads/rosalind_deg.txt').read()
nodes=[int(edge) for edge in edges.split()]
nodes=nodes[2:]
D=[]
for i in range(1,max(nodes)+1):
    D.append(nodes.count(i))

print(' '.join(map(str,D)))
print(max(nodes))
