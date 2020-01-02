k=2
m=2
n=2

from scipy.special import comb
  
total = k+m+n

dd = comb(n,2)/comb(total,2)
rr = comb(m,2)/comb(total,2)
dr = comb(n,1)*comb(m,1)/comb(total,2)

prob = 1 - (dd+rr*1/4+dr*1/2)

print (prob)
