sequence="""TCAATGCATGCGGGTCTATATGCAT"""

def reverse_complement(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1])

for i in range(len(sequence)):
    for j in range(4,12):
        if sequence[i:i+j]==reverse_complement(sequence[i:i+j]):
                print("{0} {1}".format((i+1),(j)))
