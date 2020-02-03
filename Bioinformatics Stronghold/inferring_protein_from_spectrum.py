file=open('Desktop/Downloads/rosalind_spec.txt','r')

L=[]
for line in file:
    line=line.strip()
    L.append(float(line))

aa_masses = []
for i in range(len(L) - 1):
    aa_mass = round(L[i + 1] - L[i], 4)
    aa_masses.append(aa_mass)

#diff=L[1:]-L[:-1]

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

answer=""
for i in aa_masses:
    answer+=mass[i]

print(answer)
