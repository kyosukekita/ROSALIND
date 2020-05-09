#隠れマルコフ二コフ　尤度問題

stringx="yyyyxyxxxyxxyzzxxyyxzyzxxxyzxzxxxyyyxzxzzzxyxzyxzz"
path="BABBAAABABABABAAABBABAAABBABBBBBABABAABBBABBABAABA"

Ax=0.349
Ay=0.183
Az=0.467
Bx=0.163
By=0.621
Bz=0.216

probability=1
for i in range(len(stringx)):
    if path[i]=="A" and stringx[i]=="x" :
        probability*=Ax
    elif path[i]=="A" and stringx[i]=="y":
        probability*=Ay
    elif path[i]=="A" and stringx[i]=="z":
        probability*=Az
    elif path[i]=="B" and stringx[i]=="x":
        probability*=Bx
    elif path[i]=="B" and stringx[i]=="y":
        probability*=By
    elif path[i]=="B" and stringx[i]=="z":
        probability*=Bz

print(probability)
