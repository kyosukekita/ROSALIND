def HammingDistance(seq1,seq2):
    """2つの配列が与えられ、ハミング距離がd以下であればTrue"""
    hamming=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            hamming+=1;
    print(hamming)

HammingDistance(seq1,seq2)
