genome=""
def Skew(genome):
    skews=[]
    for i in range(len(genome)):
        skew=genome[:i].count("G")-genome[:i].count("C")
        skews.append(skew)
    minim=min(skews)
    answer=[str(i) for i,v in enumerate(skews) if v==minim]
    return answer    
        
print(*Skew(genome))
