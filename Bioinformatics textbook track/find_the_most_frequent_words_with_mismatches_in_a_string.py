import itertools
import collections

def HammingDistance(seq1,seq2,d):
    """2つの配列が与えられ、ハミング距離がd以下であればTrue"""
    mismatch=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            mismatch+=1;
    return mismatch<=d   



file=open('Desktop/Downloads/rosalind_ba1i.txt').read()
dna=file.split("\n")[0]
k,d=[int(i) for i in file.split("\n")[1].split()]


kmers=[]#text中のすべてのkmerを列挙
for i in range(0,len(dna)-k+1):
    kmers.append(dna[i:i+k])

    
possible_kmers=[''.join(p) for p in itertools.product(['A','T','C','G'], repeat=k)]#考えられうるkmerを全て列挙,k回重複ＯＫ  
    

answer=[]
for i in range(len(kmers)):
    for j in range(len(possible_kmers)):
        if HammingDistance(kmers[i],possible_kmers[j],d):
            answer.append(possible_kmers[j])
            

c=collections.Counter(answer)
print(c.most_common())
