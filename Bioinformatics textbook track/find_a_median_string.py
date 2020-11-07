file=open('Desktop/Downloads/rosalind_ba2b (2).txt').read()
k=int(file.split("\n")[0])
dnas=[n for n in file.split("\n")[1:] if n!=""]


import itertools

def HammingDistance(seq1,seq2):
    """2つの配列が与えられ、ハミング距離を数える"""
    mismatch=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            mismatch+=1;
    return mismatch


def exHammingDistance(seq1,text):
    """1つの配列とテキストのdistanceのハミング距離(拡張版)を調べる"""
    k=len(seq1)
    min_dist=float("inf")
    for i in range(len(text)-k+1):
        dist=HammingDistance(seq1,text[i:i+k])
        if dist < min_dist:
            min_dist=dist
    return min_dist
 
 
patterns=[]#all kmer patterns in a text
for i in range(len(dnas)):
    for j in range(0,len(dnas[i])-k+1):
        patterns.append(dnas[i][j:j+k])

possible_kmers=([''.join(p) for p in itertools.product(['A','T','G','C'],repeat=k)])#すべてのkmer



min_dist=float("inf")


for i in range(len(possible_kmers)):
    dist=0
    for j in range(len(dnas)):
        dist+=exHammingDistance(possible_kmers[i], dnas[j])
    if min_dist>dist:
        min_dist=dist
        answer=(possible_kmers[i])
        
print(answer)
