P="0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1"
p=list(map(int,P.split()))

peptide=[]
for i in range(len(p)):
    if p[i]==1:
        peptide.append(i+1)

        
import numpy as np
weights=list(np.array(peptide[1:])-np.array(peptide[:-1]))
weights.insert(0,peptide[0])


def mass2amino(weight):
    protein_mass_table="""
A 71
C 103
D 115
E 129
F 147
G 57
H 137
I 113
K 128
L 113
M 131
N 114
P 97
Q 128
R 156
S 87
T 101
V 99
W 186
Y 163 
"""

    temp = protein_mass_table.split()
    amino_list=[str(k) for k in temp[0::2]]
    weight_list=[int(k) for k in temp[1::2]]
    
    i=weight_list.index(weight)
    
    return amino_list[i]

answer=list(map(mass2amino,weights))
print(''.join(answer))
