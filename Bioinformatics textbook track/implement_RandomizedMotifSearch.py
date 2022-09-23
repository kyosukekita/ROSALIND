
#http://www.hcbravo.org/cmsc423/lectures/Motif_finding.pdf

import random
from collections import Counter #最頻値を使うため

file=open('Desktop/Downloads/rosalind_ba2f (4).txt').read()
k,t=map(int,file.split("\n")[0].split())
dnas=[i for i in file.split("\n")[1:] if i!=""]


def hamming_distance(a,b):
    hamming=0
    for i in range(len(a)):
        if a[i] !=b[i]:
            hamming +=1
    return hamming


def Score(motifs):
    """motifsのコンセンサス配列を求めて、そのコンセンサス配列と
    どれだけ異なる文字を含んでいるかをスコアとする"""
    score=0
    
    consensus=""
    for i in range(len(motifs[0])):
        ith_lettrers_in_motifs=[]
        for motif in motifs:
            ith_lettrers_in_motifs.append(motif[i])
        consensus+=(Counter(ith_lettrers_in_motifs).most_common()[0][0])
    
    for motif in motifs:
        score+=hamming_distance(motif,consensus)
    
    return score


def FormProfile(motifs):
    profile=[[1 for _ in range(4)] for _ in range(len(motifs[0]))]#pseudocounts
    for i in range(len(motifs)):
        for j in range(len(motifs[i])):
            if motifs[i][j]=="A":
                profile[j][0]+=1
            elif motifs[i][j]=="C":
                profile[j][1]+=1
            elif motifs[i][j]=="G":
                profile[j][2]+=1
            else:
                profile[j][3]+=1
    return profile#これが次のprofile-matrixになる


def probability(matrix,sequence):
    probability=1
    for i in range(len(sequence)):
        if sequence[i]=="A":
            probability*=matrix[i][0]
        elif sequence[i]=="C":
            probability*=matrix[i][1]
        elif sequence[i]=="G":
            probability*=matrix[i][2]
        else:
            probability*=matrix[i][3]
            
    return probability


def MostProbableKmer(dnas,matrix,k):
    highest_score=-float("inf")
    for i in range(len(dnas)-k+1):
        kmer=dnas[i:i+k]
        if highest_score < probability(matrix,kmer):
            highest_score=probability(matrix,kmer)
            most_probable_kmer=kmer
    return most_probable_kmer



def MakeRandomMotifs(dnas,k):
    motifs=[]
    for dna in dnas:
        j=random.randint(0,len(dna)-k)
        motifs.append(dna[j:j+k])
    return motifs


def RandomizedMotifSearch(dnas,k,t):
    motifs=MakeRandomMotifs(dnas,k)
    BestMotifs=random_motifs
    
    while True:
        profile=FormProfile(motifs)
        motifs=[]
        for i in range(t):
            motifi=MostProbableKmer(dnas[i],profile,k)
            motifs.append(motifi)
        if Score(motifs) < Score(BestMotifs) :
            BestMotifs=motifs 
        else:
            return BestMotifs

    
best_score=float("inf")
for _ in range(1000):
    result = RandomizedMotifSearch(dnas,k,t)
    current_score = Score(result)
    if current_score <= best_score:
        best_score = current_score
        best_result = result
        
        
print('\n'.join(map(str,best_result)))
