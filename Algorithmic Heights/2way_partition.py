file = open('Desktop/Downloads/rosalind_par.txt').read()
n=int(file.split("\n")[0])
A=[int(i) for i in file.split()[1:]]


#クイックソートの原理。これで正解が出たが、おそらく偶然か？
def partition(a):
    p=a[0]
    l=[x for x in a[1:] if x<=p]
    r=[x for x in a[1:] if x>p ]
        
    return l+[p]+r

answer=partition(A)
print(' '.join(list(map(str,answer))))



#正攻法はこちら。元の配列でスワップを続ける。http://rosalind.info/problems/par/solutions/
def partition(a, n):
    x = a[0]
    p, q = 1, n-1
    while p <= q:
        if a[p] > x:
            a[p], a[q] = a[q], a[p]
            q -= 1
        else:
            a[p-1] = a[p]
            p += 1
    a[p-1] = x
    return a
