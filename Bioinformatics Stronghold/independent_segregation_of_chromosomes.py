n=45
import math
def combi(n,k):
    nCk=math.factorial(n)//math.factorial(n-k)//math.factorial(k)
    return nCk
    
A=[]
for k in range(1,2*n+1):
    prob=0
    for i in range(k,2*n+1):
        prob +=combi(2*n,i)*((0.5)**(2*n))
    Ak=math.log10(prob)
    A.append(Ak)
    
print(*A)
