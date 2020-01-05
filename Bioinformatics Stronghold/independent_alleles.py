k=5
N=8
P=2**k

def combination(n,k):
    return math.factorial(n)/ (math.factorial(k)*math.factorial(n-k))

probability=0

for i in range(0, N):
    prob = combination(P,i) * (0.25**i) * (0.75**(P - i))  
    probability +=prob
print(1-probability)
