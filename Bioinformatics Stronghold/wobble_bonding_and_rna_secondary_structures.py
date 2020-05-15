s="""AUAUGUGAUCUGUAUGACUUACCGAUAGUAGCCCAUGGGGCACUAGCUUUGGUUUACCCUU
AUUAGUACGUACUGCGGUCCUUCUAUCCUAGGCUCUGAUCCGAUCAGUAGCCGAAGGCAGCGAG
AAACACGCCCGGCGUGUGUCUUCGAUAACCUAUGGUGUGUGACGUCAUCAUC"""

cache={}
def wobble(rna):
    rna=rna.replace("\n","")
    
    if len(rna)<=4:
        return 1
    
    if rna in cache:
        return cache[rna]
    
    cache[rna]=wobble(rna[1:])
    for i in range(4,len(rna)):
        if (rna[0]=="A" and rna[i]=="U") or (rna[0]=="G" and rna[i]=="C") or(rna[0]=="G" and rna[i]=="U") or (rna[0]=="U" and rna[i]=="A") or (rna[0]=="U" and rna[i]=="G") or (rna[0]=="C" and rna[i]=="G"):
            cache[rna]+=(wobble(rna[1:i])*wobble(rna[i+1:]))
        
    return cache[rna]

wobble(s)
