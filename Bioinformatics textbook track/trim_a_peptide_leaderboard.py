file = open('/Users/kita/Downloads/rosalind_ba4l.txt', 'r').read()
#file = open('/Users/kita/Downloads/rosalind_meme.txt', 'r').read()
Leaderboard=list(str(i) for i in (file.split("\n")[0].split()))
Leaderboard=list(str(i) for i in (file.split("\n")[0].split()))
Spectrum=[int(i) for i in file.split("\n")[1].split() if i!=" "]
N=int(file.split("\n")[2])


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



def Linearspectrum(peptide):
    weights=[0]
    for i in range(len(peptide)):        
        weights.append(seq2mass(peptide[i]))

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


def scoring_function(peptide,spectrum_):
    spectrum=spectrum_.copy()
    score=0
    memory={}
    linear_spectrum=Linearspectrum(peptide)
    
    for i in linear_spectrum:
        if i in spectrum:
            if i not in memory:
                memory[i]=1
                score+=1
                spectrum.pop(spectrum.index(i))#共通していた部分は除く
            elif memory[i]<linear_spectrum.count(i):
                memory[i]+=1
                score+=1
                spectrum.pop(spectrum.index(i))#共通していた部分は除く
            else:
                continue
    
    return score   

import numpy as np

def trim(leaderboard, Spectrum, n):
    linearscores=[scoring_function(leaderboard[j], Spectrum) for j in range(len(leaderboard))]
    leaderboard=sorted(leaderboard, key= lambda x: scoring_function(x,Spectrum),reverse=True )
    linearscores=sorted(linearscores, reverse=True)
    
    boolean_id=[]
    for j in range(len(leaderboard)):
        if linearscores[j] < linearscores[n]:#ここ間違い。サンプルデータセットは不正解
            boolean_id.append(False)
        else:
            boolean_id.append(True)
    
    return "  ".join(list(np.array(leaderboard)[boolean_id]))
    
        
    
print(trim(Leaderboard, Spectrum, N))
