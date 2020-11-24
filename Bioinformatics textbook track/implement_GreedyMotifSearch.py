#http://www.hcbravo.org/cmsc423/lectures/Motif_finding.pdf

from collections import Counter #最頻値を使うため

file=open('Desktop/Downloads/rosalind_ba2d.txt').read()
k,t=map(int,file.split("\n")[0].split())
dnas=[i for i in file.split("\n")[1:] if i!=""]


def hamming_distance(a,b):
    hamming=0
    for i in range(len(a)):
        if a[i] ==b[i]:
            pass
        else:
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
    profile=[[0 for _ in range(4)] for _ in range(len(motifs[0]))]
    
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


def MostProbableKmer(dna,matrix):
    most_probable_kmer="None"
    highest_score=-1e6

    for i in range(len(dna)-k+1):#ここ+1する必要ある？
        kmer=dna[i:i+k]
        if highest_score < probability(matrix,kmer):
            highest_score=probability(matrix,kmer)
            most_probable_kmer=kmer
    
    return most_probable_kmer


def GreedyMotifSearch(dnas,k,t):
    first_kmers=[dna[:k] for dna in dnas]#motif matrix formed by first kmers in each string
    kmers_from_first_string=[dnas[0][i:i+k] for i in range(len(dnas[0])-k+1)]#1行目のDNA配列からできるkmerの一覧
    BestMotifs=kmers_from_first_string
    
    for kmer_motif in kmers_from_first_string:
        motifs=[kmer_motif]
        for i in range(1,t):
            profile=FormProfile(motifs)
            motifi=MostProbableKmer(dnas[i],profile)
            motifs.append(motifi)

        if Score(motifs) < Score(BestMotifs):
            BestMotifs=motifs
    
    return BestMotifs


BestMotifs=GreedyMotifSearch(dnas,k,t)
for i in BestMotifs:
    print(i)
