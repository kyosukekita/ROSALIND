




#これはずるい解法
file = open('Desktop/Downloads/rosalind_ba9k.txt').read()
BWT=(file.split("\n")[0])
Patterns=[tmp for tmp in file.split("\n")[1].split() if tmp!='']
LastColumn=sorted(BWT.split())


def inv_BWT(text):
    array = [x for x in range(len(text))]
    array = sorted(array, key=lambda x: text[x])
    output = ""
    
    idx = text.index('$')
    for _ in range(len(text)):
        idx=array[idx]
        output+=text[idx]
    
    return output


answer=[]
for pattern in Patterns:
    answer.append(inv_BWT(BWT).count(pattern))
    
print(" ".join(map(str,answer)))
