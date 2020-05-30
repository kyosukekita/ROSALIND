sequence=""

def revcomp(sequence):
    tmp=sequence.replace("A","X").replace("T","A").replace("X","T").replace("C","Y").replace("G","C").replace("Y","G")
    print(tmp[::-1])

revcomp(sequence)
