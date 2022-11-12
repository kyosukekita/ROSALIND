#shortest common supersequence (SCSLength(X,Y)= m+n-LCSLength(X,Y))　典型的な動的計画法だが、この問題はLCSと密接に関係している。
# https://python.plainenglish.io/print-shortest-common-supersequence-day-61-python-bba3ca1c288

s="""TTACGGCCCCTACCCGTTAGACTGCTCTTCCGTGCTTAGCGGTGTCTCGAGTATTAGTACGGCCAGCACATTTGACCGTGTATTCCGGGCTA"""
t="""AGGATAGTTTCTAAAAGCATACGAGCGATCCCTTGGATGAGAAGTCTCGACGTAGAGGAACTGCCGTTCTAGATGCCAACCAAGAGGATCGGAAAG"""

s.split()
t.split()

def SCS(x,y):
    m=len(x)
    n=len(y)
    #dpのテーブルを作る
    dp=[[0 for i in range(n+1)]
           for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1): 
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],　dp[i][j-1])

    string=""
    
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        # If current character in X and Y are same,  
        # then current character is part of 
        # shortest supersequence 
        if x[i - 1] == y[j - 1]: 
  
            # Put current character in result 
            string += x[i - 1] 
  
            # reduce values of i, j 
            i -= 1
            j -= 1
  
        # If current character in X and Y are different 
        elif dp[i - 1][j] > dp[i][j - 1]: 
  
            # Put current character of Y in result 
            string += y[j - 1] 
  
            # reduce values of j
            j -= 1

        else: 
  
            # Put current character of X in result 
            string += x[i - 1] 
  
            # reduce values of i
            i -= 1

  
    # If Y reaches its end, put remaining characters 
    # of X in the result string 
    while i > 0: 
        string += x[i - 1] 
        i -= 1
  
    # If X reaches its end, put remaining characters 
    # of Y in the result string 
    while j > 0: 
        string += y[j - 1] 
        j -= 1
  
    string = list(string) 
  
    # reverse the string and return it 
    string.reverse() 
    return ''.join(string) 

SCS(s,t)


#参考
class FindLongest:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[float('-inf') for j in range(len(text2)+1)]for i in range(len(text1)+1)]
        for i in range(len(memo)):
            for j in range(len(memo[0])):
                if i == 0 or j == 0:
                    memo[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        i = len(memo)-1
        j = len(memo[0])-1
        ans = ""
        while(i >= 0 and j >= 0):
            if text1[i-1] == text2[j-1]:
                ans += text1[i-1]
                i -= 1
                j -= 1
            else:
                if memo[i-1][j] > memo[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        return(ans[::-1])
