#選択ソート - 未ソートの部分から最小の要素を探し出し、それを未選択ソート部分の先頭と交換する
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

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

#挿入ソート - 配列を順番に走査し、各要素をそれまでのソート済みの部分に適切な位置に挿入することによって配列をソート
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def iSort(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j]>=a[j-1]:
                break #このbreak文がポイント
            else:
                a[j],a[j-1]=a[j-1],a[j]
    return a

#シェルソート
"""挿入ソートを一般化したアルゴリズムで、非連続なサブリストに対して挿入ソートを行い、徐々にソート範囲を拡大していきます"""
def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


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
