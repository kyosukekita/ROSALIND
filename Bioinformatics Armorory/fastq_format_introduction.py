from Bio.SeqIO.QualityIO import FastqGeneralIterator 
# For real speed, don't even make SeqRecord and Seq objects!

in_handle=open('Desktop/Downloads/rosalind_tfsq (1).txt', 'r')  
for title, seq, qual in FastqGeneralIterator(in_handle):
    print(">%s" % title) 
    for i in range(0, len(seq), 60): 
        print(seq[i : i + 60] ) 
        
        
        
from Bio import SeqIO
SeqIO.convert("Rosalind.txt", "fastq", "Rosalind_Output.txt", "fasta")
