def freqArray(dna,k):
    freqarray=[]
    
    kmers=[''.join(v) for v in itertools.product(['A','C','G','T'], repeat=k)]
    for kmer in kmers:
        count=0
        for i in range(len(dna)):
            if dna[i:i+k]==kmer:
                count+=1
        freqarray.append(count)
    
    return freqarray
