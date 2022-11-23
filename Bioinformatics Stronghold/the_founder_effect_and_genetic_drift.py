#参考　https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_foun.py

import math
import numpy as np


N=19; m=3
A="1 3 4 10"
A=[int(i) for i in A.split(" ")]
k=len(A)


def WrightFisher_GeneticDrift(N, m, g):#gは次の世代
    q = m/(2*N) # dominant allele
    p = 1 - q # recessive_allele

    # the probability of exactly i copies of recessive allele in 1st generation.
    prob = [math.comb(2*N,i) * (q**(i)) * (p**(2*N-i)) for i in range(1, 2*N+1)]

    # 次の世代でtコピーの recessive allele が存在する確率
    for gen in range(1, g):
        gen_prob = []

        # 第１世代から現世代までのある世代において、t コピーのrecessive allele が存在する確率
        for t in range(1, 2*N+1):
            # this generation, copies (t) of recessive allele range from 1 to 2*N.
            # last generation, copies (i) of recessive allele range from 1 to 2*N,
            # for each possible copies t, we calculated probability from i to t.
            prob_t = [math.comb(2*N,t) * ((i/(2*N))**(t)) * ((1-(i/(2*N)))**(2*N-t)) for i in range(1, 2*N+1)]
            gen_prob.append(sum([prob_t[j] * prob[j] for j in range(2*N)]))
        prob = gen_prob

    # print(np.log10(1-sum(prob)))
    return np.log10(1-sum(prob))



B=[[0 for _ in range(k)] for _ in range(m)]
for i in range(m):
    for j in range(k):
        B[i][j] = WrightFisher_GeneticDrift(N, A[j], i+1)

#答えを出力
for i in range(m):
    print(*B[i])
