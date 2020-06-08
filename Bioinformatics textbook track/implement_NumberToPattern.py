def patternToNumber(pattern):#前回作った関数
    nucleotide={"A":"00","C":"01","G":"10","T":"11"}
    
    number="0b"
    for i in range(len(pattern)):
        number += nucleotide[pattern[i]]
    return (int(number,2))
    
    

def NumberToPattern(index,k):
    candidates=[''.join(v) for v in itertools.product(['A','C','G','T'], repeat=k)]#重複あり順列
        
    for pattern in candidates:
        if patternToNumber(pattern)==index:
            return(pattern)
