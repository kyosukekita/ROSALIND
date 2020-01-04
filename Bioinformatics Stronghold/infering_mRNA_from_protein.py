protein= open('rosalind_mrna.txt', 'r').read()
protein=list(protein)

string = """F 2 L 6 I 3 M 1 V 4 S 4 P 4 T 4 A 4 Y 2 H 2 Q 2 N 2 K 2 D 2 E 2 C 2 W 1 R 6 S 6 G 4"""

traL = string.split()
amino_list=[ i for i in traL[0::2]]
codon_list=[int(i) for i in traL[1::2]]

d=dict(zip(amino_list, codon_list))

count=3 #number of stop codon
for amino in protein:
    if amino in d.keys():#辞書が空ならエラー
        count *=d[amino]
   
print(count%1000000)
