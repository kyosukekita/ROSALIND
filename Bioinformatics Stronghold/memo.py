#1

toy=["abc","bcd","cde"]
ses=[]
for i in range(len(toy)):
    sess=""
    for nt in toy[i]:
        sess +=nt
        ses.append(sess)
print(ses)

#2

for i in range(len(toy)):
    sess=""
    for nt in toy[i]:
        sess +=nt
        print(sess)

