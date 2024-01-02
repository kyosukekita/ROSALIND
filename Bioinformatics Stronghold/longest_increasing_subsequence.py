def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    # LISの長さを記録する配列を初期化
    lis = [1] * len(arr)

    # 各要素についてLISを計算
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # 最大のLISの長さを返す
    return max(lis)

# 例
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print("Longest Increasing Subsequence Length:", longest_increasing_subsequence(arr))



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


#別解
def lgis(n, π):
    S = [[]]*(n+1)
    for i in π:
        S[i] = max(S[:i], key=len)+[i]
    print(S)
    return ' '.join(map(str, max(S, key=len)))

print(lgis(5, permutation_list)) 
