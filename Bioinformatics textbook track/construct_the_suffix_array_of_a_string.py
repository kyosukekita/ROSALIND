text=""

def SuffixArray(text):
    numbering={}
    k=0
    
    #各接尾辞と番号の対応表を作成しておく
    for i in range(len(text)):
        numbering[text[i:]]=k
        k+=1
    
    suffixArray=sorted([text[i:] for i in range(len(text))])
    
    answer=[]
    for i in range(len(suffixArray)):
        answer.append(numbering[suffixArray[i]])
    
    
    
    return answer

print(", ".join(map(str,SuffixArray(text))))

