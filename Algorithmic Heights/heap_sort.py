file = open('Desktop/Downloads/rosalind_hs (1).txt').read()
n=int(file.split()[0])
A=[int(i) for i in file.split()[1:n+1]]

from heapq import heappush
from heapq import heappop

def linked_heap_sort(arr):
    heap=[]
    while arr:
        heappush(heap,arr.pop())
    while heap:
        arr.append(heappop(heap))
        
    return (arr)
        
print(' '.join(list(map(str,linked_heap_sort(A)))))




#正解は出せるが、速度が非常に遅くて間に合わない解法。
def maxheap(arr,i):
    for i in range(1,n):
        j=i
        while j >0:
            if arr[j]>arr[(j-1)//2]:
                arr[j],arr[(j-1)//2]=arr[(j-1)//2],arr[j]
                j=(j-1)//2
            else:
                break 
    return arr


answer=[]
while n!=0:  
    maximum=maxheap(A,n)[0]
    answer.append(maximum)
    A=[A[-1]]+A[1:-1]
    n-=1
    
print(' '.join(list(map(str,answer[::-1]))))
