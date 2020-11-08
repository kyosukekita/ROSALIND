#動的計画法 古典的なおつり問題
#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja
#https://muttan1203.hatenablog.com/entry/2017/05/30/155343

file = open('Desktop/Downloads/rosalind_ba5a.txt').read()
total=int(file.split("\n")[0])
coins=[int(i) for i in file.split("\n")[1].split(",")]

def combinations1(coins,total):
    dp=[float("inf")]*(total+1)#dp[i]:i円払うときの最小の枚数
    dp[0]=0
    
    
    for i in range(len(coins)):
        for j in range(total-coins[i]+1):
            dp[j+coins[i]]=min(dp[j+coins[i]],dp[j]+1)
    
    return (dp[-1])


print(combinations1(coins,total))
