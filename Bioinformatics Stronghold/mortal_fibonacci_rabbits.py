#Fn=Fn-1+Fn-2-Fn-(m+1)

n=80
m=16


def mortalFibonacci(n,m):
    ages=[1]+[0]*(m-1) #k歳のウサギの数を数える。ウサギの歳はm通り。
    for i in range(n-1):
        ages=[sum(ages[1:])]+ages[:-1]#子供たち+その親たち
    return sum(ages)

mortalFibonacci(n,m)
