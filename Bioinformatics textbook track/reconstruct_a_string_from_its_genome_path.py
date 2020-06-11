file = open('Desktop/Downloads/rosalind_ba3b.txt', 'r').read()
dnas=[i for i in file.split("\n")]

genome=dnas[0]
for i in range(1,len(dnas)):
    genome+=dnas[i][-1]

print(genome)
