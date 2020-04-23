#http://rosalind.info/problems/pcov/solutions/

strings= open('Desktop/Downloads/rosalind_pcov.txt').read()
strings=[i for i in strings.split()]

k=len(strings[0])-1#k-mer
d={}

#de Bruijin graph
for string in strings:
    d[string[:k]]=string[1:]
#cycle from graph
R=[]
root=strings[0][:k]
child=root
while True:
    R.append(child)
    child=d[child]
    if child ==root:
        break

genome=""
for r in R:
    genome +=r[0]
print(genome)

"""
genome assembly as shortest superstringで用いた方法は使えない。この問題は
環状のperfect coverageを求めているので、片方向からしか配列を足せない。
"""
