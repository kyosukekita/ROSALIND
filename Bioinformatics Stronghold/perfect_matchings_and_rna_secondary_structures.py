import math

RNA="""AGCUAGUCAU
"""

AU=RNA.count("A")
GC=RNA.count("G")

matchings =math.factorial(AU)*math.factorial(GC) #complete bipartite graph
print(matchings)
