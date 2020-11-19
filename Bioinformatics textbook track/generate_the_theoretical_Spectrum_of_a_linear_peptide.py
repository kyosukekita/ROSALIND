peptide="HGLFDNLMVVPCVYNWQNLTDGANFESGSPFVESGICGNILGDYFHK"

protein_mass_table="""
A 71 C 103 D 115
E 129 F 147 G 57
H 137 I 113 K 128
L 113 M 131 N 114
P 97 Q 128 R 156
S 87 T 101 V 99
W 186 Y 163 
"""
temp = protein_mass_table.split()
weight_list=[int(k) for k in temp[1::2]]
amino_list=[str(k) for k in temp[0::2]]
mass_table=dict(zip(amino_list, weight_list))    


def LinearSpectrum(peptide):
    weights=[0]
    for i in range(len(peptide)):        
        weights.append(mass_table[peptide[i]])
    
    #累積和のテクニック
    cumsum=[0]
    for weight in weights[1:]:
        cumsum.append(cumsum[-1]+weight)
   
    spectrum=[0]
    for i in range(len(weights)):
        for j in range(i+1,len(weights)):
            spectrum.append(cumsum[j]-cumsum[i])
    spectrum.sort()
    
    return (spectrum)

print(" ".join(map(str,LinearSpectrum(peptide))))
