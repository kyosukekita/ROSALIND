file = open('Desktop/Downloads/rosalind_2sum.txt').read()
k,n=[int(i) for i in file.split("\n")[0].split()]
B=[int(i) for i in file.split()[2:]]

A=[]
for i in range(0,len(B),n):
    A.append(B[i:i+n])


answer=[]
for a in A:
    tmp=[]
    flag=False
    for p in range(n):
        for q in range(p+1,n):
            if a[p]+a[q]==0:
                tmp.append([p+1,q+1])
                flag=True
                
    
    if flag:
        answer.append(tmp[-1])
    else:
        answer.append([-1])


for i in answer:
    print(' '.join(map(str,i)))
