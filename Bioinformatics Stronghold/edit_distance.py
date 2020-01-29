#Levenshtein distance

file = open('Desktop/Downloads/rosalind_edit.txt', 'r').read()

sequence_list=[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    seq = ''.join(parts[1:])
    sequence_list.append(seq)
s=sequence_list[0]
t=sequence_list[1]
    
import Levenshtein
print(Levenshtein.distance(s,t))
