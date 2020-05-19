N=90000
GCcontent=0.6
dna="""ATAGCCGA"""

AT=dna.count("A")+dna.count("T")
GC=dna.count("G")+dna.count("C")

string_probability=((1-GCcontent)/2)**AT*(GCcontent/2)**GC
probability=1-(1-string_probability)**N
print("{:.3f}".format(probability))



#シミュレーションによる別解
"""指定されたdnaと同じ長さのdnaをN回生成し、そのなかに一つでも指定されたdna
が含まれる場合をカウントする。"""
import numpy as np

N=90000
GCcontent=0.6
dna="""ATAGCCGA"""

J=5 #ここではＪ=5としたが、Jの値を∞に増大させると理論的には上の解法と同じ値が出てくる。

count=0 
for _ in range(J):
    candidates=[]
    for _ in range(N):
        random_string=""
        for _ in range(len(dna)):
            k=np.random.choice(["A", "T", "G", "C"], p=[(1-GCcontent)/2,(1-GCcontent)/2, GCcontent/2, GCcontent/2])
            random_string += str(k)
        candidates.append(random_string)

    if dna in candidates:
        count+=1

    
print(count/J)
