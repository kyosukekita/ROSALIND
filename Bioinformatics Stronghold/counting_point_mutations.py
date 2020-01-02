A="GGAGATAGGGGGGATGAAGATCCCCG"
B="GGAGCTAGGGAGGATGAAGATTCCCG"

hamming=0
for i in range(len(A)):
    if A[i]==B[i]:
        pass
    else:
        hamming =hamming+1
print(hamming)
