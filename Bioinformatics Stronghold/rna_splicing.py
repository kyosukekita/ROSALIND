
file = open('Desktop/Downloads/rosalind_splc.txt', 'r').read()

d={}
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    fasta = parts[0]
    seq = ''.join(parts[1:])
    d[fasta]=seq

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

sequence=list(d.values())

for intron in sequence[1:]:
    if intron in  sequence[0]:
        sequence[0]=sequence[0].replace(intron,'')
print(translate(sequence[0]))
