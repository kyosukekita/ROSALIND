S="57 71 154 185 301 332 415 429 486"
s.insert(0,0)


diff=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        diff.append((s[i],s[j]))


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
mass=dict(zip(weight_list, amino_list))



for i in diff:
    if (i[1]-i[0]) in mass.keys():
        print(str(i[0])+"->"+str(i[1])+":"+mass[i[1]-i[0]])
