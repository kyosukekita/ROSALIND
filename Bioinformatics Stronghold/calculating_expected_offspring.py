file=open('rosalind_iev.txt','r')
for line in file:
    str_line=str(line)
    val=str_line.split()

import numpy as np
way=np.array(val,dtype=np.int32)
probability=np.array([1,1,1,float(0.75),float(0.5),0])
expect=way*probability*2
print(np.sum(expect))
