    
dna="""
CCTTCCCGGGCACATCCCTGGCCCGATAACACTCGAGAACTTTAATGTTACCACGGGTGT
ACGGCGTTGCACAGCAAAGGTTGTAAAAGCGTATCAAGTCGGAAAAAGGCAACACTCGAA
CCGCGATGACATCGTGGTAGGAAAGGGGGCTACAAGTCAGTGTCGTGTACGGCCTGTGCG
GGGAACTCAGGGTAGTCAATTACGGCCTAGCACCCTGAAGTCCGCCGAAGCCGGAAAAGG
CTACTGCGCTGGATATACTCTTGTTACAACCGGGTATGCATTTGAGAGCCTCGAAATATA
CCCTAAATCCACATCCACGGCTTACCCTTACTACGGTGGGCATATTCGTACCCTTGCCCA
TACTCAGCTCAATTTTCTAACCTTCTGTTCGCACAGTCCTGCGTAATGCCTGAATCAAGA
GATGCGGGGGTAAGCCCATACATAGCTATGTATGGGCTTACCCCCGCATGGCTAATTACT
TGCGATCCCAAACGGCTCCGGGGGCCGACTACCTTAGGGAGTTTGTGCTCAGGTTTTTTA
GTGGAAACGACGATCTCGTATGCGACGGTTGGTTATGCGACCGTATTATAATTGAGGCGT
AAGGTGTGAGCTGTCTATATGAGCTTACCGCAGGTTTGACACCTCGTCGCATTGGTTAAA
CAACTTAAACAGGCCTTCATCCCCCACCGGGGATAATTACCGTGTCGCATGCCCAGACTT
TAGCACCACCTTTCAAGGTATGGCTACCGTCTGCCGCCGTGTGTCACGTGATGGTTTTTC
ACAAGATAACGACAGTCGGTCGGTTAGGATGAGACCCCCACGGACCACTCCAAACGTTGC
GACGTATCGTGATCTCAAACCTGGTTCATGGGTACGTTTATAGTTTTGTG"""

dna=dna.replace("\n","")

def translate(seq): 
    decoded=""
    string = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA *      CAA Q      AAA K      GAA E
TAG *      CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA *      CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G"""
    
    temp=string.split()
    codon_map=dict(zip(temp[0::2], temp[1::2]))    
    for i in range(0, len(seq)-3, 3):
        decoded += codon_map[seq[i:i+3]]
    return decoded

def reverse_complement(sequence):
    temp=sequence.replace("A","x").replace("T","A").replace("x","T")
    return (temp.replace("G","x").replace("C","G").replace("x","C")[::-1])



open_reading_frames=[]
for i in range(0,len(dna)):
    if dna[i:].startswith("ATG"):
        for j in range(0,len(dna[i:]),3):
            if  dna[i:][:j].endswith("TAG") or dna[i:][:j].endswith("TAA") or dna[i:][:j].endswith("TGA") :
                open_reading_frames.append(dna[i:][:j])

dna_r=reverse_complement(dna)

for i in range(0,len(dna_r)):
    if dna_r[i:].startswith("ATG"):
        for j in range(0,len(dna_r[i:]),3):
            if  dna_r[i:][:j].endswith("TAG") or dna_r[i:][:j].endswith("TAA") or dna_r[i:][:j].endswith("TGA") :
                open_reading_frames.append(dna_r[i:][:j])             

for i in set(open_reading_frames):
    if "*" in translate(i):
        pass
    else:
         print(translate(i))
