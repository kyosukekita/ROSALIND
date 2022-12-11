#https://courses.grainger.illinois.edu/cs466/sp2020/slides/Lecture5_WeightedSeqeunceAlignment.pdf
#https://www.el-kebir.net/teaching/CS466/Fall_2019/lecture3.pdf
#https://valiec.github.io/AlignmentVisualizer/index.html

import numpy as np

file = open('/Users/kita/Downloads/rosalind_ba5h (1).txt').read()
v=file.split("\n")[0]
w=file.split("\n")[1]


def fitting_alignment(s,t):
    s=s.replace("\n","")
    t=t.replace("\n","")
    
    dp=[[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]
    
    for i in range(len(t)+1):
        for j in range(len(s)+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=-i
            
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i]==s[j] :
                dp[i+1][j+1] = max(dp[i][j+1]-1 , dp[i+1][j]-1, dp[i][j]+1)
            else:
                dp[i+1][j+1] = max(dp[i][j+1]-1 , dp[i+1][j]-1,dp[i][j]-1)
                    
    #print(dp[len(dp)-1])
    
    i=len(t)#dpの一番後ろの列
    j=np.argmax(dp[i])
    maximum=dp[i][j]
    
    s_align=""
    t_align=""
    #Begin with the highest score, end when 0 is encountered
    while (i>0):
        if t[i-1]==s[j-1] and dp[i][j]==dp[i-1][j-1]+1:
            s_align += s[j-1]
            t_align += t[i-1]
            i -= 1
            j -= 1
        
        elif dp[i][j]==dp[i][j-1]-1:
            s_align += s[j-1]
            t_align +="-"
            j-=1
        elif dp[i][j]==dp[i-1][j]-1:
            s_align +="-"
            t_align += t[i-1]
            i -= 1
        elif t[i-1]!=s[j-1] and dp[i][j]==dp[i-1][j-1]-1:
            s_align += s[j-1]
            t_align += t[i-1]
            i -= 1
            j -= 1
        
        else:
            break

    print(maximum)
    print(s_align[::-1])
    print(t_align[::-1])

fitting_alignment(v,w)
