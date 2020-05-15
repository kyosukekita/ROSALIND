peptides= open('Desktop/Downloads/sample.txt').read()
peptides=[float(i) for i in peptides.split()]
n=int(len(peptides)/2)-1

def mass_to_peptides(spectrum):
    protein_mass_table="""
A 71.0371
C 103.0092
D 115.0269
E 129.0426
F 147.0684
G 57.0215
H 137.0589
I 113.0841
K 128.0950
L 113.0841
M 131.0405
N 114.0429
P 97.0528
Q 128.0586
R 156.1011
S 87.0320
T 101.0477
V 99.0684
W 186.0793
Y 163.0633 
"""
    temp = protein_mass_table.split()
    weight_list=[float (k) for k in temp[1::2]]
    amino_list=[str(k) for k in temp[0::2]]
    mass=dict(zip(weight_list, amino_list))

    pairs=[]
    for x in range(1,len(spectrum)):
        for y in range(x+1,len(spectrum)):
            if abs(spectrum[0]-spectrum[x]-spectrum[y])< 0.001:
                pairs.append((spectrum[x], spectrum[y]))   
    
    sequence=""
    index=0
    while index < n:
        nearest_candidate = None
        
        for i in mass.keys():
            if abs(pairs[index+1][0]-pairs[index][0]-i)< 0.0001:
                nearest_candidate=i

        if nearest_candidate is None:  #(if not nearest_candidate)
            pairs[index+1]=(pairs[index+1][1], pairs[index+1][0])
            pairs.sort()
        else:
            sequence+= mass[nearest_candidate]
            index +=1
                     
    return sequence


print(mass_to_peptides(peptides))
