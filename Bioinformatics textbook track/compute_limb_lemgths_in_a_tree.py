#https://www.cs.cmu.edu/~02251/lectures/Evo_Trees_Math.pdf
"""If D is an additive matrix and j is a leaf in Tree(D), then
LimbLength(j) is equal to the minimum value of (Di, j + Dj, k − Di, k)/2 over all leaves i and k of Tree(D),"""

file = open('Desktop/Downloads/rosalind_ba7b.txt').read()
n=int(file.split("\n")[0])
j=int(file.split("\n")[1])
D=[[int(k) for k in tmp.split()] for tmp in file.split("\n")[2:] if tmp!='']

candidates=[]
for i in range(n):
    for k in range(n):
        tmp=(D[i][j]+D[j][k]-D[i][k])/2
        if tmp>0:
            candidates.append(tmp)

print(int(min(candidates)))
