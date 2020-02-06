path="""BBBAAAAAAABBABBABBBBBBAAAAABAABABBBBABBBBAABABBBBB"""

AA=0.062
AB=0.938
BA=0.554
BB=0.446

probability=0.5
for i in range(len(path)-1):
    if path[i]=="A" and path[i+1]=="A":
        probability=probability*AA
    elif path[i]=="A" and path[i+1]=="B":
        probability=probability*AB
    elif path[i]=="B" and path[i+1]=="A":
        probability=probability*BA
    else:
        probability=probability*BB

print(probability)
