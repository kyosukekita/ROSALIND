file=open('rosalind_revc.txt','r')
for line in file:
    str_line=str(line)

def reverse_complement(sequence):
    temp=sequence.replace("A","x").replace("T","A").replace("x","T")
    return (temp.replace("G","x").replace("C","G").replace("x","C")[::-1])

reverse_complement(str_line)
