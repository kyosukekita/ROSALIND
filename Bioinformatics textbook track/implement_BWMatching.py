file = open('Desktop/Downloads/rosalind_ba9k.txt').read()
BWT=(file.split("\n")[0])
Patterns=[tmp for tmp in file.split("\n")[1].split() if tmp!='']
LastColumn=BWT


def last_to_first(text,i):
    first = [x for x in range(len(text))]
    first = sorted(first, key=lambda x: text[x])
    output = ""
    
    idx = text.index('$')
    for _ in range(len(text)):
        before=idx
        idx = first[idx]
        if idx==i:
            return before
        

def BWMatching(LastColumn, Pattern):
    text=LastColumn
    
    top=0
    bottom=len(LastColumn)-1
    
    while top <= bottom:
        if len(Pattern)!=0: #if Patternという書き方もできる
            symbol=Pattern[-1]
            Pattern=Pattern[:-1]
            
            
            tmp=LastColumn[top:bottom+1]
            reverse=tmp[::-1]
            
            if symbol in tmp:
                topIndex=tmp.find(symbol)+top#findはindexとほとんど同じだが、指定する文字列が無い場合-1を返す
                bottomIndex=len(tmp)-reverse.find(symbol)-1+top
                top=last_to_first(text,topIndex)
                bottom=last_to_first(text,bottomIndex)
            
            else:
                return 0
        
        else:
            return bottom -top+1
    

answer=[]
for pattern in Patterns:
    answer.append(BWMatching(LastColumn, pattern))
print(" ".join(map(str,answer)))




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
