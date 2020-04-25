dna="""CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG"""
dna=dna.replace("\n","")

from itertools import product
table={}
for kmer in product('ACGT', repeat=4):
    table[''.join(kmer)]=0

for i in range(len(dna)-4+1):
    kmer=dna[i:i+4]
    table[kmer] +=1
    
for i in table.values():
    print(i, end= ' ') #end=' 'で改行無し

    
 
"別解"
import collections
import itertools as it

def kmerComposition(dna, k):
    return collections.Counter([dna[i:i+k] for i in range(len(dna)-k+1)]) #辞書型

kmers = kmerComposition(dna, 4)
for kmer in [''.join(s) for s in it.product('ACGT', repeat=4)]:
    print(kmers[kmer], end=" ")
