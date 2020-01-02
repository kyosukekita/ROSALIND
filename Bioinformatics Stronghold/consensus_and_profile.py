file=open('rosalind_cons.txt').read()

collection=[]
for seqlock in file.split(">")[1:]:
    parts=seqlock.split("\n")
    string=''.join(parts[1:])
    collection.append(string)

list_A=[0]*len(collection[0])
list_C=[0]*len(collection[0])
list_G=[0]*len(collection[0])
list_T=[0]*len(collection[0])

for i in range(len(collection[0])):
    for j in range(10):
        if collection[j][i]=="A":
            list_A[i] +=1
        elif collection[j][i]=="C":
            list_C[i] +=1
        elif collection[j][i]=="G":
            list_G[i] +=1
        else:
            list_T[i] +=1

consensus=[]
for i in range(len(collection[0])):
    base=max(list_A[i],list_C[i],list_G[i],list_T[i])
    if base == list_A[i]:
        consensus.append("A")
    elif base == list_C[i]:
        consensus.append("C")
    elif base == list_G[i]:
        consensus.append("G")
    else:
        consensus.append("T")

print(''.join(consensus))
print("A: "+ ' '.join(map(str,list_A)))
print("C: "+ ' '.join(map(str,list_C)))
print("G: "+ ' '.join(map(str,list_G)))
print("T: "+ ' '.join(map(str,list_T)))
