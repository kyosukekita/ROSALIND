#find_a_k-universal_circular_string.py
#reconstruct_a_string_from_its_kmer_composition.pyの続き,de-bruijin graphを使う、オイラー経路の問題
k=4

import itertools
from collections import defaultdict

kmers=[]#すべてのkmerをリストアップ  別解[bin(i)[2:].zfill(k) for i in range(2**k)]
aa=itertools.product([0,1],repeat=k)
for a in aa:
    kmers.append("".join(map(str,a)))

nodes=defaultdict(list)#de bruijin graph ここをdefaultdictにしたのは、キーが無くてもいけるから
for kmer in kmers:
    if kmer!="1"+"0"*(k-1) or kmer!="0"*k:
        nodes[kmer[:-1]].append(kmer[1:])
        nodes[kmer[1:]].append(kmer[:-1])#反対向きエッジも入れる


#cycle from graph
tour=[]
start=kmers[0][:-1]#000
tour.append(start)

while(len(nodes[start])>0):
    estart=start[1:len(start)]#00
    if estart+"1" in nodes[start]:#001
        tour.append(estart+"1")
        nodes[start].remove(estart+"1")
        nodes[estart+"1"].remove(start)
        start=estart+"1"
    else:
        tour.append(estart+"0")#000
        nodes[start].remove(estart+"0")
        nodes[estart+"0"].remove(start)
        start=estart+"0"

answer="0"
for _, d in enumerate(tour):
    answer+=d[0]

print(answer)





#https://heyglobal.tistory.com/3
def circularString(lastpoint):
    lastpointZero =  lastpoint [1:k] + '0'
    if  lastpointZero  not in  partString:
        partString.append(lastpointZero)
        totalString.append(0)
        circularString(lastpointZero)
    lastpointOne =  lastpoint [1:k] +  '1'
    if  lastpointOne  not  in  partString:
        partString.append(lastpointOne)
        totalString.append(1)
        circularString(lastpointOne)
    if  len(partString)== 2 ** k:
        return  totalString
    else:
        totalString.pop()

k=8
totalString = []
partString = []
partString.append(k* '0')
for i in range(k):
    totalString.append(0)
lastpoint =  partString [0]
print(''.join(map(str,circularString(lastpoint))))





#https://algorithmcode.wordpress.com/2014/11/18/string-reconstruction/
from collections import defaultdict
import collections   
import itertools

in_binary= 4
lpos = in_binary-1

last_binary ='1'*in_binary
bin_int = int(last_binary, 2)

last_before = "1"+('0'*lpos)
first = '0'*in_binary
nodes = defaultdict(list)
for i in range(0,bin_int+1):
    a = (bin(i)[2:].zfill(in_binary))
    if (a!=last_before and a!=first):
        s = a[0:lpos]
        e = a[1:in_binary]
        #print a, s,e
        nodes[s].append(e)
        nodes[e].append(s)
print(nodes)       
        
tour = []
start = '0'*(in_binary-1)
tour.append(start)
while(len(nodes[start])>0):
    estart = start[1:len(start)]
    if estart+"1" in  nodes[start]:
        tour.append(estart+"1")
        nodes[start].remove(estart+"1")
        nodes[estart+"1"].remove(start)
        start = estart+"1"
    else:
        tour.append(estart+"0")
        nodes[start].remove(estart+"0")
        nodes[estart+"0"].remove(start)
        start = estart+"0"      

ou_res ='0'
for i,d in enumerate(tour):
    ou_res+=d[0]

print (ou_res)
