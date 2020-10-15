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

#ヒープソート
def heap_sort(array):
    i=0
    n=len(array)
    
    while(i<n):
        #ヒープを構成
        upheap(array,i)
        i +=1
        
    while(i>1):
        #ヒープから最大値を取り出し
        i -=1
        tmp=array[0]
        array[0]=array[i]
        array[i]=tmp
        
        #ヒープの再構成
        downheap(array,i-1)
        
#array[n]をヒープ構成部(0~n-1)の最適な位置へ移動
def upheap(array,n):
    while n!=0:
        parent=int((n-2)/2)
        if array[n]>array[parent]:
            tmp=array[n]
            array[n]=array[parent]
            array[parent]=tmp
        else:
            break
            
#ルート「0」をヒープ構成部(0~n)の最適な位置へ移動
def downheap(array,n):
    if n==0:
        return
    parent=0
    while True:
        child=2*parent+1
        
        if child >n:
            break
        if (child<n) and array[child] <array[child+1]:
            child +=1
        if array[parent] < array[child]:
            tmp=array[child]
            array[child]=array[parent]
            array[parent]=tmp
            parent = child
        esle:
            break
           
#デバッグ
if __name__=="__main__":
    array=[1,2,3,4,5,3,2,1,4,3,4,5,0]
    print("befroe",array)
    heap_sort(array)
    print("after",array)            
