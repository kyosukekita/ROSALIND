stringx="xyxzzxyxyy"

"""transition"""
AA=0.641
AB=0.359
BA=0.729
BB=0.271


"""Emission"""
Ax=0.117
Ay=0.691
Az=0.192
Bx=0.097
By=0.42
Bz=0.483


probabilities=[]
path=""

#初期
if stringx[0]=="x":
    probabilities.append((Ax,Bx))
elif stringx[0]=="y":
    probabilities.append((Ay,By))
else:
    probabilities.append((Az,Bz))

#再帰処理
for i in range(1,len(stringx)):
    lastA,lastB=probabilities[-1]
    if stringx[i]=="x":
        thisA=max(lastA*AA*Ax,lastB*BA*Ax)
        thisB=max(lastA*AB*Bx,lastB*BB*Bx)
        probabilities.append((thisA,thisB))
    elif stringx[i]=="y":
        thisA=max(lastA*AA*Ay,lastB*BA*Ay)
        thisB=max(lastA*AB*By,lastB*BB*By)
        probabilities.append((thisA,thisB))
    else:
        thisA=max(lastA*AA*Az,lastB*BA*Az)
        thisB=max(lastA*AB*Bz,lastB*BB*Bz)
        probabilities.append((thisA,thisB))

#最適状態系列の復元
for p in probabilities:
    if max(p[0],p[1])==p[0]:
        path+=("A")
    elif max(p[0],p[1])==p[1]:
        path+=("B")
        
print(path)
