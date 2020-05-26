P="THEVFQKQEHLMKYANNVTPGKLLLETHFRLTEG"

def aminomass(amino):
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
    
    i=amino_list.index(amino)
    
    return weight_list[i]


P=list(map(aminomass, P))


def cumsum(xs):
    """累積和"""
    result=[xs[0]]
    for x in xs[1:]:
        result.append(result[-1]+x)
    return result

answer=[0]*(cumsum(P)[-1])
for i in cumsum(P):
    answer[i-1]=1

print(' '.join(map(str,answer)))
