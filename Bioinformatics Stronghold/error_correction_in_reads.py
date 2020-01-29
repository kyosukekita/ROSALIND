import itertools

file = open('Desktop/Downloads/rosalind_corr (1).txt').read()
sequence_list=[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    seq = ''.join(parts[1:])
    sequence_list.append(seq)   

def reverse_complement(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1]) 

def hamming_distance(a,b):
    hamming=0
    for i in range(len(a)):
        if a[i] ==b[i]:
            pass
        else:
            hamming +=1
    return hamming

correct=[]
for i,j in (itertools.combinations(range(len(sequence_list)),2)):
    if reverse_complement(sequence_list[i])== sequence_list[j]:
        correct.append(sequence_list[i])
        correct.append(sequence_list[j])
    elif sequence_list[i]==sequence_list[j]:
        correct.append(sequence_list[i])
        correct.append(reverse_complement(sequence_list[i]))
    else:
        pass
    
answer={}
for i in range(len(sequence_list)):
    for j in range(len(correct)):
        if hamming_distance(sequence_list[i],correct[j]) ==1:
            answer[sequence_list[i]]=correct[j]

for k, v in answer.items():
    print("{0}->{1}".format(k,v))
