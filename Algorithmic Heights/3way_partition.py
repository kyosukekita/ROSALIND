file = open('Desktop/Downloads/rosalind_par3.txt').read()
n=int(file.split("\n")[0])
A=[int(i) for i in file.split()[1:]]

#これも2wayの時と同じで、permutationを使ってないから邪道か？
def par3(a):
    p=a[0]
    count=a.count(p)
    l=[x for x in a[1:] if x<p]
    r=[x for x in a[1:] if x>p ]
        
    return l+[p]*count+r

answer=par3(A)
print(' '.join(list(map(str,answer))))
