file = open('Desktop/Downloads/rosalind_ps.txt').read()
n=int(file.split()[0])
A=[int(i) for i in file.split()[1:n+1]]
k=int(file.split()[-1])

from heapq import heappush
from heapq import heappop

def linked_heap_sort(arr):
    heap=[]
    while arr:
        heappush(heap,arr.pop())
    while heap:
        arr.append(heappop(heap))
        
    return (arr)
        
print(' '.join(list(map(str,linked_heap_sort(A)[:k]))))
