file=open('Desktop/Downloads/rosalind_ba2h.txt').read()
pattern=file.split("\n")[0]
Dna=file.split("\n")[1].split()


def hamming_distance(a,b):
    hamming=0
    for i in range(len(a)):
        if a[i] ==b[i]:
            pass
        else:
            hamming +=1
    return hamming


def DistanceBetweenPatternAndStrings(pattern,Dna):
    k=len(pattern)
    distance=0
    
    for Text in Dna:
        HammingDistance=float("inf")
        Pattern_in_Text=[Text[i:i+k] for i in range(len(Text)-k+1)]
        
        for pattern1 in Pattern_in_Text:
            if HammingDistance > hamming_distance(pattern,pattern1):
                HammingDistance = hamming_distance(pattern,pattern1)
                
        distance=distance+HammingDistance
    
    return distance
                

DistanceBetweenPatternAndStrings(pattern,Dna)
