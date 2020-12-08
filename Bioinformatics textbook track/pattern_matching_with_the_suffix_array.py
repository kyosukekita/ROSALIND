file = open('Desktop/Downloads/rosalind_ba9h.txt').read()
text=(file.split("\n")[0])
patterns=[i for i in file.split("\n")[1:] if i!=""]


def SuffixArray(text,patterns):
    numbering={}
    k=0
    
    for i in range(len(text)):
        numbering[text[i:]]=k
        k+=1
    
    suffixArray=sorted([text[i:] for i in range(len(text))])
    
    answer=[]
    for pattern in patterns:
        for suffix in suffixArray:
            if suffix.startswith(pattern):
                answer.append(numbering[suffix])
     
    return sorted(answer)

print(" ".join(map(str, SuffixArray(text,patterns))))
