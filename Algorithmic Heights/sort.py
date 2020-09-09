#選択ソート
def sSort(a):
    for i in range(len(a)-1):
        mi=a[i:].index(min(a[i:]))
        a[i],a[i+mi]=a[i+mi],a[i]
    
    return a

#バブルソート
def bSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1,i,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1]=a[j-1],a[j]
    
    return a

#挿入ソート
def iSort(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j]>=a[j-1]:
                break #このbreak文がポイント
            else:
                a[j],a[j-1]=a[j-1],a[j]
    return a

#クイックソート
def qSort(a):
    if len(a) in (0,1):
        return a
    
    p=a[-1]
    l=[x for x in a[:-1] if x<=p]
    r=[x for x in a[:-1] if x>p]

    return qSort(l)+[p]+qSort(r)

#マージソート
def merge(l,r):#マージ
    n=len(l+r) #マージ後の配列のサイズ
    s=max(l+r)+1 #番兵

    l.append(s)
    r.append(s)

    a=[]
    while len(a)<n:
        a.append(l.pop(0)) if l[0]<=r[0] else a.append(r.pop(0))

    return a


def mSort(a):#分割
    if len(a)==1:
        return a

    mid=len(a)//2
    l=mSort(a[:mid])
    r=mSort(a[mid:])

    return merge(l,r)

