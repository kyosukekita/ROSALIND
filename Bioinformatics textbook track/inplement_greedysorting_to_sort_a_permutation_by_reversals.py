#http://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1103&context=etd_projects

file=open('Desktop/Downloads/rosalind_ba6a.txt').read()
P=[int(i) for i in file.strip("()").split()]

def transpositions(P,k):
    j=k#例えばkが0だとして、
    while P[j]!=k+1 and P[j]!=-(k+1):#P[0]が1でも-1でもなかったら、
        j+=1
    P[k:j+1]=list(map(lambda x: -x, P[k:j+1][::-1]))#リストPの中で、P[0]と隣のP[1]を入れ替える
    return P

def greedySorting(P):
    reversals=[]
    for k in range(len(P)):#例えばk=0だとして、
        while P[k] !=k+1:#P[0]のところに1が来るまで、永遠に回す
            P=transpositions(P,k)
            reversals.append(list(P))
    return reversals


results = greedySorting(P)
for result in results:
    print("(" + " ".join(["+" + str(x) if x > 0 else str(x) for x in result]) + ")")
