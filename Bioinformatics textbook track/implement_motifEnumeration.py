"""問題の指示とは異なる方法の解法"""

import itertools
import collections

def HammingDistance(seq1,seq2,d):
    """2つの配列が与えられ、ハミング距離がd以下であればTrue"""
    mismatch=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            mismatch+=1;
    return mismatch<=d

def wordsWithmismatch(seq1,d):
    """配列が一つ与えられると、ハミング距離がd以下である配列をリストで返す"""
    answer=[]
    possible_kmers=[''.join(p) for p in itertools.product(['A','T','C','G'], repeat=len(seq1))]
    for i in range(len(possible_kmers)):
        if HammingDistance(seq1,possible_kmers[i],d):
            answer.append(possible_kmers[i])
        
    return answer
    
 

#データ読み込み
file=open('Desktop/Downloads/rosalind_ba2a.txt').read()
k,d=[int(i) for i in file.split("\n")[0].split()]
dnas=file.split("\n")[1:]



def MotifEnumeration(dnas,k,d):
    patterns=set([''.join(p) for p in itertools.product(['A','T','C','G'], repeat=k)])#kmerを全て書きだしておく
    
    for i in range(len(dnas)):
        kmer=[]#ある一つのDNA配列について、kmerを全て書き出す
        for j in range(len(dnas[i])-k+1):
            kmer.append(dnas[i][j:j+k])
        
        mismatch=[]
        for j in range(len(list(kmer))):
            mismatch +=wordsWithmismatch(kmer[j],d)#書き出したkmerについて、ハミング距離がd以内の配列を全て書き出す。
            
        mismatch=set(mismatch)#重複を除去
    
        patterns = patterns & mismatch#重複する項だけがpatternsに残っていく。

    
    return ' '.join(map(str,list(patterns)))


print(MotifEnumeration(dnas,k,d))
