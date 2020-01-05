import itertools
alphabet="A B C"
alphabet=(alphabet.split())

N=3

v=[''.join(v) for v in itertools.product(alphabet, repeat=N)]#重複あり順列

for i in v:
    print(i)
