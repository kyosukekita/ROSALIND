pattern="GGTAAATGGC"
text=""

d=6


def HammingDistance(seq1,seq2,d):
    """2つの配列が与えられ、ハミング距離がd以下であればTrue"""
    mismatch=0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            mismatch+=1;
    return mismatch<=d


answer=[]
for i in range(len(text)-len(pattern)+1):
    if HammingDistance(text[i:i+len(pattern)],pattern,d):
        answer.append(i)
        
print(' '.join(map(str,answer)))
