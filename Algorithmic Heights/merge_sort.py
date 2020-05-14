def merge(l,r):
    answer=[]
    
    while len(l)!=0 and len(r)!=0:
        if l[0] <=r[0]:
            answer.append(l.pop(0))
        else:
            answer.append(r.pop(0))
    
    if len(l)!=0:
        answer.extend(l)
    if len(r)!=0:
        answer.extend(r)
    
    return answer
    
    
    
def mergeSort(a):
    if len(a)==1:
        return a
    
    mid=len(a)//2
    l=mergeSort(a[:mid])
    r=mergeSort(a[mid:])
    return merge(l,r)


A=""

A=[int(i) for i in A.split()]

a=' '.join(map(str,mergeSort(A)))
print(a)
