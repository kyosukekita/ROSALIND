#マンハッタン観光客問題-動的計画法

file = open('Desktop/Downloads/rosalind_ba5b.txt').read()
n,m=int(file.split()[0]), int(file.split()[1])


D=[]
for i in range(0,n*m,m+1):
    D.append(file.split()[2:][i:i+(m+1)])

R=[]
for i in range(0,(n+1)*m,m):
    R.append(file.split()[3+n*(m+1):][i:i+m])

    

def manhattan(down,right,n,m):
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][0]=dp[i-1][0]+int(down[i-1][0])
    for j in range(1,m+1):
        dp[0][j]=dp[0][j-1]+int(right[0][j-1])
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=max(dp[i-1][j]+int(down[i-1][j]), dp[i][j-1]+int(right[i][j-1]))
    
    return dp[n][m]

manhattan(D,R,n,m)
