file = open('rosalind_grph.txt', 'r').read()

d = {}
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    d[fasta]=seq

import itertools
sequence_list=list(d.keys())
for i,j in (itertools.permutations(range(len(sequence_list)),2)):
     if sequence_list[i][-3:]==(sequence_list[j][:3]) and sequence_list[i] !=sequence_list[j]:
        print(d[sequence_list[i]], d[sequence_list[j]])   
