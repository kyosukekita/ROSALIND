n=871894
s="""CGACAGTAG"""
A="""0.000 0.085 0.131 0.171 0.231 0.285 0.364 0.403 0.492 0.510 0.589 0.624 0.667 0.759 0.784 0.837 0.930 1.000"""
A=[float(i) for i in A.split()]

def main(s,A,n):
    AT=s.count("A")+s.count("T")
    GC=s.count("G")+s.count("C")
    B=[]
    if len(s) > n:
        pass
    else:
        for i in range(len(A)):
            string_probability=((1-A[i])/2)**AT*(A[i]/2)**GC
            B.append(str((string_probability*(n-len(s)+1)))) #n-len(s)+1 回現れる。      
    
    return B

answer=' '.join(main(s,A,n))
print(answer)
