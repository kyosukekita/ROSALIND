file = open('Desktop/Downloads/rosalind_ba4f.txt', 'r').read()
peptide=str(file.split("\n")[0])
spectrum=[int(i) for i in file.split("\n")[1].split() if i!=" "]


def seq2mass(sequence):
    """ペプチド配列の分子量を算出"""
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
    weight_list=[int (k) for k in temp[1::2]]
    amino_list=[str(k) for k in temp[0::2]]
    mass_table=dict(zip(amino_list, weight_list))

    total_mass=0
    for i in list(sequence):
        total_mass+=mass_table[i]

    return total_mass



def Cyclospectrum(peptide):
    subst=["",(peptide)]
    length=len(peptide)
    tmp=peptide+peptide
    
    for i in range(0,length):
        for j in range(1,length):
            subst.append(tmp[i:i+j])

    spectrum=[seq2mass(i) for i in subst]

    return sorted(spectrum)


def scoring_function(peptide,spectrum):
    score=0
    memory={}
    cyclic_spectrum=Cyclospectrum(peptide)
    
    for i in cyclic_spectrum:
        if i in spectrum:
            if i not in memory:
                memory[i]=1
                score+=1
                spectrum.pop(spectrum.index(i))#共通していた部分は除く
            elif memory[i]<cyclic_spectrum.count(i):
                memory[i]+=1
                score+=1
                spectrum.pop(spectrum.index(i))#共通していた部分は除く
            else:
                continue
    
    return score


print(scoring_function(peptide,spectrum))
