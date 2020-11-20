#問題文の誘導とは異なるが、
"""動的計画法の部分和問題 n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から何個かの整数を選んで総和が A になるようにする方法が何通りあるかを求めよ"""
#https://qiita.com/drken/items/a5e6fe22863b7992efdb
#https://qiita.com/gushwell/items/02a6ee994eacf3d9d3e0 ←でもこれ複数種あった時対応できないよね？


import itertools
file = open('Desktop/Downloads/rosalind_ba4e.txt').read()
spectrum=[int(i) for i in file.split()]
total=spectrum[-1]#427
collections=spectrum[:-1]#[0,113,128,186,241,299,314]

dp=[-1 for _ in range(total+1)]#初期値は-1だから、dp[i] !=-1 は部分和がiになるときの組み合わせが存在するということ
dp[0]=0

for collection in collections:
    for i in range(total,-1,-1):
        if dp[i]==-1:
            continue
        
        if (i+collection<=total and dp[i+collection]==-1):
            dp[i+collection]=collection
    
    if dp[total]!=-1:
        break


def toResult(dp,total):
    result=[]
    if dp[total]!=-1:
        while total>0:
            result.append(dp[total])
            total-=dp[total]
    
    return result

result=toResult(dp,total)#[186,128,112]の3つの合計がtotalの分子量と一致する。


def Cyclospectrum(peptide):
    spectrum=[0,sum(peptide)]
    length=len(peptide)
    tmp=peptide+peptide

    for i in range(0,length):
        for j in range(1,length):
            subst=(tmp[i:i+j])
            spectrum.append(sum(subst))
    return sorted(spectrum)


def selection(result,spectrum):
    answers=[]
    #resultから受けとったリストの順列を作成する。そのcyclospectrumが問題文で与えられたspectrumならばOK.
    for v in itertools.permutations(result):
        if Cyclospectrum(list(v))==spectrum:
            answers.append(list(v))
    
    return answers


answers=selection(result,spectrum)
for answer in answers:
    print("-".join(map(str,answer)), end=" ")
