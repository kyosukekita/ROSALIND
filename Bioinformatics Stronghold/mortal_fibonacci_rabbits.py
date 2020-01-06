#Fn=Fn-1+Fn-2+Fn-(m+1)

n=80
m=16


def mortalFibonacci(n,m):
    ages=[1]+[0]*(m-1)
    for i in range(n-1):
        ages=[sum(ages[1:])]+ages[:-1]
    return sum(ages)

mortalFibonacci(n,m)
