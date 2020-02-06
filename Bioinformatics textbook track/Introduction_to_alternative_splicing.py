import math

n=1885
m=952

answer=0
for k in range(m,n+1):
    Cnk=math.factorial(n)//(math.factorial(n-k)*math.factorial(k))
    answer +=Cnk

#Overflow error
#import sys sys.float_info.max  -> 1.7976931348623157e+308

print(answer%1000000)
