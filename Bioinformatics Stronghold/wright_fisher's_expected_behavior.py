n=17
P="0.1 0.2 0.3"
P=[float(i) for i in P.split()]

import math
def expectation(k):
    return n*k

B=list(map(expectation,P))
print(' '.join(map(str,B)))
