file = open('Desktop/Downloads/rosalind_qs.txt').read()
n=int(file.split()[0])
A=[int(i) for i in file.split()[1:n+1]]


def qSort(a):#クイックソート
    if len(a) in (0,1):
        return a
    
    p=a[-1]
    l=[x for x in a[:-1] if x<=p]
    r=[x for x in a[:-1] if x>p ]
    
    return qSort(l)+[p]+qSort(r)

answer=qSort(A)
print(' '.join(list(map(str,answer))))
