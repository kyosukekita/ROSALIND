n,k=21,7

result=1
for i in range(k):
    result *=n-i
    result %=1000000
print (result)
