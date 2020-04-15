import itertools

n=6
a = itertools.permutations(range(1,n+1))
print(len(list(a))*2**n)


def signedPermutations(n):
    for perm in itertools.permutations(range(1,n+1)):
        for signed_perm in itertools.product(*[(-element, element) for element in perm]):
            yield signed_perm

for i in signedPermutations(n):
    print(*i)



#Sara does bioinformatics(http://saradoesbioinformatics.blogspot.com/2016/07/enumerating-oriented-gene-orderings.html)

import itertools                                                           
n = 3                                                                      
permutation = []                                                           
nr = 0                                                                     
for i in itertools.permutations(list(range(1, n + 1))):                    
    for j in itertools.product([-1, 1], repeat=len(list(range(1, n + 1)))):
        perm = [a * sign for a, sign in zip(i, j)]                         
        permutation.append(perm)                                           
        nr += 1                                                            

print(nr)                                                                  

for i in range(len(permutation)):                                          
    print(*permutation[i], sep=' ')    
