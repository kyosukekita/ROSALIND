from multiprocessing import Process

file = open('Desktop/Downloads/rosalind_laff.txt', 'r').read()
d =[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    d.append(seq)


def local_align_with_affine(s,t):
    s=s.replace('\n','')
    t=t.replace('\n','')
   
    import pandas as pd
    BLOSUM62=pd.DataFrame([
    [4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
    [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
    [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
    [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
    [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
    [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
    [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
    [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
    [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
    [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
    [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
    [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
    [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
    [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
    [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
    [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
    [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
    [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
    [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]],
    index=['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'],
    columns=['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
 
    dp=[[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
    x=[[0 for j in range(len(t)+1)] for i in range(len(s)+1)] #s aligned to a gap
    y=[[0 for j in range(len(t)+1)] for i in range(len(s)+1)] #t aligned to a gap
    
    for i in range(1,len(s) + 1):
        y[i][0]=(-1)*(i-1)-11
    for i in range(1, len(t) + 1):
        x[0][i]= (-1)*(i-1)-11

    maximum=0
    s_start=0
    t_start=0
    
    for i in range(1, len(s)+1):
        for j in range(1,len(t)+1):
            cost=BLOSUM62[s[i-1]][t[j-1]]            
            x[i][j]=max(dp[i-1][j]-11, x[i-1][j]-1)
            y[i][j]=max(dp[i][j-1]-11, y[i][j-1]-1)
            
            dp[i][j] = max(0,dp[i-1][j-1]+cost, x[i][j],y[i][j])
            
            if dp[i][j]>maximum:
                maximum=dp[i][j]
                s_start=i
                t_start=j
    
    print(maximum)
    
    s_align=''
    t_align=''
    i=s_start
    j=t_start
    
    while (i>0 and j>0):
        if dp[i][j] ==dp[i-1][j-1]+BLOSUM62[s[i-1]][t[j-1]]:
            s_align = s[i-1]+s_align
            t_align =t[j-1]+t_align
            i -= 1
            j -= 1
        elif i>0 and dp[i][j]==x[i][j]:
            s_align = s[i-1]+s_align
            t_align ='-'+t_align
            i -=1
        elif j>0 and dp[i][j]==y[i][j]:
            t_align =t[j-1]+t_align
            s_align ='-' +s_align
            j -= 1
        elif dp[i][j]==0:
            break

        print(s_align)
        print(t_align)

local_align_with_affine(d[0],d[1])
