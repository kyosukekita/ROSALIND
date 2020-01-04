import math   
def probability(s, A):
    n = s.count("G") + s.count("C")
    return([(len(s)-n)*math.log10(1-gc) + n*math.log10(gc) - len(s)*math.log10(2) for gc in A])

string='GAGGGCAAAGAACCCGTGGCCAAGCTTAGTCTCCTCAGGTGGTACAAGGGCCCTTCGGTGGTCTCCTAGGCACGTGACATTCAGCGTCATCA'
A= [0.115, 0.153, 0.247, 0.287, 0.374, 0.408, 0.445, 0.506, 0.590, 0.633, 0.745, 0.753, 0.866, 0.895]

probability(string, A)
