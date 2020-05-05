#1

toy=["abc","bcd","cde"]
ses=[]
for i in range(len(toy)):
    sess=""
    for nt in toy[i]:
        sess +=nt
        ses.append(sess)
print(ses)

#2

for i in range(len(toy)):
    sess=""
    for nt in toy[i]:
        sess +=nt
        print(sess)
        
        
        
def catalan(n):
    Cn=(math.factorial(2*n)/(math.factorial(n)**2)/(n+1))#Cn=2nCn/(n+1)
    return int(Cn)

