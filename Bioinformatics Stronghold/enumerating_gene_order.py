import itertools

n = 7
a = list(itertools.permutations(range(n)))
print(len(a))

for i in a:
    for j in i:
        print("{} ".format(j+1), end="")
    print()
