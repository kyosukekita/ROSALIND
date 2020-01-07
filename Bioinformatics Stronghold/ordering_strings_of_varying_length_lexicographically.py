import itertools
alphabet="X A S O L K Q V Y R Z"
alphabet=alphabet.replace(' ','')

n=4

perm=[]
for i in range(1,n+1):
    perm.append(list(''.join(v) for v in itertools.product(alphabet, repeat=i)))

perm2=[]
for i in perm:
    perm2 += i

sort_perm = sorted(perm2, key=lambda x: [alphabet.index(c) for c in x]) #アルファベット順

with open('answer.txt','w') as f:
    for i in sort_perm:
         f.write('%s\n' % i)
