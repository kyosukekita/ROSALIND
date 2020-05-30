file= open('Desktop/Downloads/rosalind_sgra.txt').read()
spectrum=[float(i) for i in file.split()]



def mass2amino(mass):#分子量からそのアミノ酸を推定する
    protein_mass_table="""
A 71.03711 C 103.00919 D 115.02694 E 129.04259
F 147.06841 G 57.02146 H 137.05891 I 113.08406
K 128.09496 L 113.08406 M 131.04049 N 114.04293
P 97.05276 Q 128.05858 R 156.10111 S 87.03203
T 101.04768 V 99.06841 W 186.07931 Y 163.06333
"""
    temp = protein_mass_table.split()
    weight_list=[float (k) for k in temp[1::2]]
    amino_list=[str(k) for k in temp[0::2]]
    mass_table=dict(zip(weight_list, amino_list))

    hit=False
    for i in mass_table.keys():
        if abs(mass-i)<0.001:
            nearest_weight=i
            hit=True
    
    if (hit):
        return mass_table[nearest_weight]
    else:
        return None



def Graph(spectrum):#スペクトラムからペプチド内アミノ酸の候補を出す
    spectrumGraph=[]
    for i in range(0,len(spectrum)):
        for j in range(i+1,len(spectrum)):
            diff=(spectrum[j]-spectrum[i])
            if mass2amino(diff):
                spectrumGraph.append([i,j,mass2amino(diff)])
    return spectrumGraph

graph=Graph(spectrum)
"""
[[0, 2, 'W'], [2, 3, 'M'], [3, 4, 'S'],
[3, 5, 'Q'], [4, 6, 'P'], [4, 7, 'Q'], 
[5, 7, 'S'], [6, 8, 'G']]
"""


def Path(graph):#引数は、1.ノード1, 2.ノード2, 3.1と2の間のエッジ(アミノ酸)
    """グラフの情報をもとに、考えられるペプチド配列を全て出す"""
    node = 0
    peptide_list = []
    tmp_edges = []
    peptide = ''
    tmp_peps = []
    
    while any([len(x) != 0 for x in tmp_edges]) or len(tmp_edges) ==0:
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
            #break サンプルデータセットの場合、ここにbreakをつけないとエラーが起きる

    return peptide_list


peptide_list=Path(graph)

        
peptide_list.sort(key=len)
print(peptide_list[-1])
