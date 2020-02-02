file = open('Desktop/Downloads/rosalind_pdst.txt').read()

sequence_list=[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    seq = ''.join(parts[1:])
    sequence_list.append(seq)

def p_distance(a,b):
    hamming=0
    for i in range(len(a)):
        if a[i] != b[i]:
            hamming +=1
        else:
            pass
    return round((hamming/len(a)),3)  

def matrix_distance(sequences):
    matrix=[[0 for _ in range(len(sequences))] for _ in range(len(sequences))]  #matrix=[[0]*len(sequences)]*len(sequences)は使えない！https://www.sejuku.net/blog/67215
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            matrix[i][j]=p_distance(sequences[i], sequences[j])
    return matrix
        
for i in matrix_distance(sequence_list):
    print(*i)
