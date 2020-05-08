s="""GUUUGUGUGUGACAGAUCAUCGGUCUAUGGUUACAGUGUGCAUGUCUUGGACACCACCAA
GAGUCGGACCUUACACCAAACUCUGGCUGCCAAAUCAUAGUGACCAUCAGUGAACUGGGC
GACUGUGGUGACACGAAUGUUAACUAAGUAAUCUUAUGUCCCGGAAAGUGUGACCCCUAU
CCAUUUAGGCGAUACGCUCUUACCGAUAAUCCGCGGUCCUGCCGGAAUCUUUGCUAUCUC
UAGAAUGGGU"""


cache={}
def motzkin(rna):
    rna=rna.replace("\n","")
    
    if rna in cache:
        return cache[rna]
    
    if len(rna)==0 or len(rna)==1:
        return 1 

    cache[rna]=motzkin(rna[1:])
    for i in range(1,len(rna)):
        if(rna[0]=="A" and rna[i]=="U") or(rna[0]=="G" and rna[i]=="C") or (rna[0]=="C" and rna[i]=="G") or (rna[0]=="U" and rna[i]=="A"):
            cache[rna]+=(motzkin(rna[1:i])*motzkin(rna[i+1:]))
            
    cache[rna]%=(10**6)
    return cache[rna]

motzkin(s)
