A=""
B=""

A=[int(i) for i in A.split()]
B=[int(i) for i in B.split()]
n=len(A+B)

answer=[]

while len(A) !=0 and len(B) !=0:
    if A[0] <=B[0]:           
        answer.append(A.pop(0))     
    else:
        answer.append(B.pop(0))
        
if len(A)!=0:
    answer.extend(A)
    
if len(B)!=0:
    answer.extend(B)

print(*answer)
