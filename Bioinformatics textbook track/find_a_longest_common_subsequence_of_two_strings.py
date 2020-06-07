def LCS(a,b):
    a=a.replace("\n","")
    b=b.replace("\n","")
    
    dp=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1]= dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    
    index=dp[len(a)][len(b)]
    lcs=[""]*(index+1)
    lcs[index]=""
    
    i=len(a)
    j=len(b)
    
    while i>0 and j>0:
        
        if a[i-1]==b[j-1]:
            lcs[index-1]=a[i-1]
            i-=1
            j-=1
            index-=1
        
        elif dp[i-1][j] > dp[i][j-1]: 
            i-=1
        else: 
            j-=1
        
    print(''.join(lcs))
