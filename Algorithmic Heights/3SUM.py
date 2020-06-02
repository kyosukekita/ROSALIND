#https://en.wikipedia.org/wiki/3SUM
file = open('Desktop/Downloads/rosalind_3sum.txt').read()
k,n=[int(i) for i in file.split("\n")[0].split()]
A=[int(i) for i in file.split()[2:]]

def qSort(a):#クイックソート
    if len(a) in (0,1):
        return a
    
    p=a[-1]
    l=[x for x in a[:-1] if x<=p]
    r=[x for x in a[:-1] if x>p ]
    
    return qSort(l)+[p]+qSort(r)

   
for i in range(0,len(A),n):
    a=A[i:i+n]
    flag=False
    copy=a.copy()#ソートする前に値を保持しておく
    a=qSort(a)#ソートをするときにクイックソートをすることで高速化している。
    tmp=[]
    for i in range(n-2):
        l=i+1#left
        r=n-1#right
        while l<r:           
            total=a[i]+a[l]+a[r]
            if total==0:
                tmp.append([copy.index(a[i])+1,copy.index(a[l])+1,copy.index(a[r])+1])
                flag=True
                break
            elif total>0:
                r-=1
            elif total<0:
                l+=1
        if flag:
            break

    if tmp:
        print(' '.join(map(str,sorted(tmp[0]))))
    else:
        print(-1)
