file=open('Desktop/Downloads/rosalind_ba6b.txt').read()
P=[int(i) for i in file.strip("()").split()]


def calcNumBreakpoints(perm):
    n=len(perm)
    num_of_breakpoints=0
    
    for i in range(n-1):
        num1,num2=perm[i:i+2]
        if abs(num1-num2)!=1:
            num_of_breakpoints+=1
    
    if perm[0]!=1:
        num_of_breakpoints+=1
    if perm[-1]!=n:
        num_of_breakpoints+=1
        
    return num_of_breakpoints
    
    
print(calcNumBreakpoints(P))  
