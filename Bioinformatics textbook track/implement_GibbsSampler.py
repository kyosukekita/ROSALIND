#正しい値に収束しない

import random
from collections import Counter #最頻値を使うため

file=open('/Users/kita/Downloads/rosalind_meme.txt').read()
k,t,N=map(int,file.split("\n")[0].split())
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
  
#https://github.com/nutstick/rosalind/blob/master/ba2g.py
def ProfileRandomKmer(Seq, profile, k):
    probs = []
    for i in range(len(Seq) - k + 1):
        Sum = 1
        for j in range(k):
            if Seq[i+j]=="A":
                ij=0
            elif Seq[i+j]=="C":
                ij=1
            elif Seq[j+j]=="G":
                ij=2
            else:
                ij=3
            Sum *= (profile[j][ij])
        probs.append(Sum)
    
    x = random.choices(list(range(0, len(Seq) - k + 1)), weights=probs)
    kmer=Seq[x[0]:x[0]+k]
    
    return kmer
        
    
def MakeRandomMotifs(dnas,k):
    motifs=[]
    for dna in dnas:
        j=random.randint(0,len(dna)-k)
        motifs.append(dna[j:j+k])
    return motifs


def GibbsSamper(dnas,k,t,N):
    motifs=MakeRandomMotifs(dnas,k)
    BestMotifs=motifs
    
    for _ in range(N):
        idx= random.randint(0,t-1)
        profile = FormProfile([motif for i, motif in enumerate (motifs) if i!=idx])
        kmer= ProfileRandomKmer(dnas[idx], profile, k)
        motifs[idx]=kmer
        
        current_score=Score(BestMotifs)
        if Score(motifs) < current_score:
            BestMotifs = motifs
            current_score=Score(motifs)
        
        return BestMotifs
        

        
best_score=float("inf")
for _ in range(２０):
    result = GibbsSamper(dnas,k,t,N)
    if Score(result) <= best_score:
        best_score = Score(result)
        best_result = result
        
        
print('\n'.join(map(str,best_result)))
  
