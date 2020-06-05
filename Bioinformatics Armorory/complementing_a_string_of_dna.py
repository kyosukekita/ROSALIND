file = open('Desktop/Downloads/rosalind_rvco.txt', 'r').read()
sequences =[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    sequences.append(seq)
    
def reverse_complement(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1])

count=0
for i in range(len(sequences)):
    if reverse_complement(sequences[i])==sequences[i]:
        count+=1

print(count)
