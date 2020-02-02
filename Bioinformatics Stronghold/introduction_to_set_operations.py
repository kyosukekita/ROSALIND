n=17511
setA={}
setB={}

setT=set(range(1,n+1))

print(setA|setB)
print(setA&setB)
print(setA-setB)
print(setB-setA)
print(setT-setA)
print(setT-setB)

"""print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(set(range(1,n+1)).difference(a))
print(set(range(1,n+1)).difference(b))
"""
