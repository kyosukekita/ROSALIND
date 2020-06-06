file = open('Desktop/Downloads/rosalind_hea.txt').read()
n=int(file.split()[0])
A=[int(i) for i in file.split()[1:n+1]]


def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    return arr


def maxheap(arr,i):
    for i in range(1,n):
        j=i
        while j >0:
            if arr[j]>arr[(j-1)//2]:#例えば子が5,6の時、親は2
                swap(arr,j,(j-1)//2)
                j=(j-1)//2
            else:
                break
    
    print(' '.join(list(map(str,arr))))

maxheap(A,n)
