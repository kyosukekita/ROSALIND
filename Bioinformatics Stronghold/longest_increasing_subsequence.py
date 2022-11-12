permutation="""5 1 4 2 3""" 

permutation=permutation.split()
permutation_list=[int(i) for i in permutation]

#最長増加部分列
import bisect
def longest_increasing_subsequence(seq):
    LIS=[seq[0]]
    for i in seq[1:]:
        if i >LIS[-1]:
            LIS.append(i)
        else:
            LIS[bisect.bisect_left(LIS,i)]=i #https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3   
    return len(LIS)

#LISそのものは最長増加部分列になっているわけではないので注意。


#正解
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


#別解
def lgis(n, π):
    S = [[]]*(n+1)
    for i in π:
        S[i] = max(S[:i], key=len)+[i]
    print(S)
    return ' '.join(map(str, max(S, key=len)))

print(lgis(5, permutation_list)) 
