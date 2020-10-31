import Bio
from Bio import SeqIO

threshold=20

count=0
for seq in SeqIO.parse("Desktop/Downloads/sample.fastq", "fastq"):
    ave=sum(seq.letter_annotations["phred_quality"])/len(seq)
    if ave <threshold:
        count+=1

print(count)
