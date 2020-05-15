file = open('Desktop/Downloads/rosalind_sexl.txt').read()
A=[float(i) for i in file.split()]

B=[]
for k in range(len(A)):
    p=A[k]
    q=1-p
    B.append(2*p*q)
    
print(' '.join(map(str,B)))
