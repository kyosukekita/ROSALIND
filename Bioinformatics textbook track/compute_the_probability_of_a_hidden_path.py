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



#compute the probability of a hidden path

hidden_path="AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB"

AA=0.194
AB=0.806
BA=0.273
BB=0.727

prob=0.5
path=""
for i in range(0, len(hidden_path)-1):
    if hidden_path[i:i+2]=="AA":
        prob*=AA
    elif hidden_path[i:i+2]=="AB":
        prob*=AB
    elif hidden_path[i:i+2]=="BA":
        prob*=BA
    elif hidden_path[i:i+2]=="BB":
        prob*=BB
    path+=hidden_path[i]
        
print(prob)
print(path)
