s="""
GAGUCGACACUCGCCGGGCAUAUAGGAUCUUGUACAUAUAAAUUAUGGAAUUCGUAUACC
GCGUACUAUCGAUAGAGUAAUCUCGCUGACGCGCCGGUCAGAACGGCUGCUUAACGCGUA
UAUAUCCGGCUCUAGUUAAAUGGCUUAAAGCUCAUCGACGGCUGUACAUAGCUAUAGCUC
GGGUAGAUCUAUAGCCUCAUGCGAAUUGGCCAAUGCCAUAGCUCGCCAAUUGAGCGCGCC
GUUACGUACGAAGCUUUUAACG
"""
s=s.replace("\n","")

dp={}
def noncrossingPerfectMatching(rna):
    if rna in dp:
        return dp[rna]
    
    if len(rna)==0 or len(rna)==1:
        return 1 

    temp=0
    for i in range(1,len(rna),2):
        if(rna[0]=="A" and rna[i]=="U") or(rna[0]=="G" and rna[i]=="C") or (rna[0]=="C" and rna[i]=="G") or (rna[0]=="U" and rna[i]=="A"):
            temp +=(noncrossingPerfectMatching(rna[1:i])*noncrossingPerfectMatching(rna[i+1:]))
    dp[rna]=temp%(10**6)
    
    return dp[rna]

noncrossingPerfectMatching(s)
