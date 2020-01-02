n=5
k=3

def fibonacci(n,k):
    a,b=1,1
    for i in range(2,n):
        a,b=b,k*a+b
    return b

fibonacci(n,k)
