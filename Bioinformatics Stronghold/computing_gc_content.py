#Biopython

from Bio import SeqIO
from Bio.SeqUtils import GC

GCcont = 0
ID = ""

file = open("rosalind_GC.txt", "r")
for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
       ID = record.id

print(ID)
print(str(round(GCcont,2))+"%")



#dictionary

file = open('rosalind_gc.txt', 'r').read()

d = {}

for seqblock in raw.split(">")[1:]:
  parts = seqblock.split("\n")
  id = parts[0]
  seq = ''.join(parts[1:])
  gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
  dic[gc] = id
print(dic[max(d)])
print(max(d))
