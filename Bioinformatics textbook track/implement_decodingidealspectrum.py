S="57 71 154 185 301 332 415 429 486"
spectrum=list(map(int,S.split()))

#アミノ酸と分子量のテーブルを作成
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
amino_list=[str(k) for k in temp[0::2]]
weight_list=[int(k) for k in temp[1::2]]
mass=dict(zip(weight_list,amino_list))



def Graph(spectrum):
    """スペクトラムからペプチド内アミノ酸の候補"""
    spectrum.insert(0,0)
    spectrumGraph=[]
    for i in range(0,len(spectrum)):
        for j in range(i+1,len(spectrum)):
            weight=(spectrum[j]-spectrum[i])
            if weight in mass.keys():
                spectrumGraph.append([spectrum[i],spectrum[j],mass[weight]])
    return spectrumGraph



def Path(graph):#引数は、1.質量スペクトラム1, 2.質量スペクトラム2, 3.1と2から推察されるアミノ酸
    """グラフの情報をもとに、考えられるペプチド配列を全て出す"""
    node = 0
    peptide_list = []
    tmp_edges = []
    peptide = ''
    tmp_peps = []
    
    while any([len(x) != 0 for x in tmp_edges]) or len(tmp_edges) == 0:
        next_edges = [e for e in graph if e[0] == node]
        if len(next_edges) > 1:
            tmp = next_edges[1:]
            tmp_edges.append(tmp)
            tmp_peps.append(peptide)
        
        next_edge = next_edges[0]
        peptide += next_edge[2]
        node = next_edge[1]
    
        if len([e for e in graph if e[0] == node]) == 0:
            tmp = [x for x in tmp_edges if len(x) != 0][-1]
            next_edge = tmp.pop()
            node = next_edge[1]
            peptide_list.append(peptide)
            tmp_pep = tmp_peps.pop()
            peptide = tmp_pep + next_edge[2]

    return peptide_list  



def idealSpectrum(peptide):
    weights=[0]
    for i in range(len(peptide)):        
        index=amino_list.index(peptide[i])
        weight=weight_list[index]
        weights.append(weight)
    
    #累積和のテクニック
    cumsum=[0]
    for weight in weights[1:]:
        cumsum.append(cumsum[-1]+weight)
   
    spectrum=[]
    for i in range(len(weights)):
        for j in range(i+1,len(weights)):
            spectrum.append(cumsum[j]-cumsum[i])
    spectrum.sort()
    
    return (spectrum)
  
    
graph=Graph(spectrum)
"""
[[0, 57, 'G'], [0, 71, 'A'], [57, 154, 'P'], [57, 185, 'Q'], [71, 185, 'N'], 
[154, 301, 'F'], [185, 332, 'F'], [301, 415, 'N'], [301, 429, 'Q'], [332, 429, 'P'],
[415, 486, 'A'], [429, 486, 'G']]
"""

peptide_candidate=Path(graph)
"""['GPFNA', 'GPFQG', 'GQFPG']"""

for peptide in peptide_candidate:
    if set(spectrum[1:]).issubset(idealSpectrum(peptide)):#部分集合であるか確認
        print(peptide)
