import itertools
import collections


def HammingDistance(seq1,seq2,d):
    """2つの配列が与えられ、ハミング距離がd以下であればTrue"""
    mismatch=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            mismatch+=1;
    return mismatch<=d


def reverse_complement(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1]) 


def wordsWithmismatch(seq1,d):
    """配列が一つ与えられると、ハミング距離がd以下である配列をリストで返す"""
    answer=[]
    possible_kmers=[''.join(p) for p in itertools.product(['A','T','C','G'], repeat=len(seq1))]
    for i in range(len(possible_kmers)):
        if HammingDistance(seq1,possible_kmers[i],d):
            answer.append(possible_kmers[i])
        if HammingDistance(seq1,reverse_complement(possible_kmers[i]),d):
            answer.append(possible_kmers[i])
        
    return answer


file=open('Desktop/Downloads/rosalind_ba1j (3).txt').read()
dna=file.split("\n")[0]
k,d=[int(i) for i in file.split("\n")[1].split()]


kmers=[]#text中のすべてのkmerを列挙
for i in range(0,len(dna)-k+1):
    kmers.append(dna[i:i+k])
    

answer={}
for i in range(len(kmers)):
    mismatch_words=wordsWithmismatch(kmers[i],d)
    for mismatch_word in mismatch_words:
        if mismatch_word not in answer:
            answer[mismatch_word]=1
        else:
            answer[mismatch_word]+=1
        
    
print(sorted(answer.items(), key=lambda x:x[1],reverse=True))
