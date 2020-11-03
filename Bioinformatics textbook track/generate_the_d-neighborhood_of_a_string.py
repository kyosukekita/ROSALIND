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
        
    return answer


file=open('Desktop/Downloads/rosalind_ba1n.txt').read()
dna=file.split("\n")[0]
d=int(file.split("\n")[1])

answers=wordsWithmismatch(dna,d)
for answer in answers:
    print(answer)
