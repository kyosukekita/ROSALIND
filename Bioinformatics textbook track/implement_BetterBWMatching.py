#制限時間ぎりぎりだった...
file = open('Desktop/Downloads/rosalind_ba9m (1).txt').read()
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


def Count(symbol,n,text):
    return text[:n].count(symbol)


def FirstOccurrence(text,symbol):
    """returns the first position of symbol in firstColumn"""
    return sorted(text).index(symbol)



def BetterBWMatching(LastColumn, Pattern):
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
                top=FirstOccurrence(text,symbol)+Count(symbol,top,LastColumn)
                bottom=FirstOccurrence(text,symbol)+Count(symbol,bottom+1,LastColumn)-1
            else:
                return 0
        
        else:
            return bottom -top+1
    

answer=[]
for pattern in Patterns:
    answer.append(BetterBWMatching(LastColumn, pattern))
print(" ".join(map(str,answer)))
