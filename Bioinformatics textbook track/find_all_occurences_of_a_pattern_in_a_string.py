pattern=""
genome=""

positions=[]
for i in range(len(genome)):
    if genome[i:].startswith(pattern):
        positions.append(i)
        
print(*positions)
