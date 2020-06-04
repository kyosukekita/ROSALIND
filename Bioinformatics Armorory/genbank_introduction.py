from Bio import Entrez
Entrez.email="myemail.com"
#db: "nucleotide" for Genbank, "pubmed" for Pubmed
handle = Entrez.esearch(db="nucleotide", term='"Vicia"[Organism] AND "2001/10/30"[PDAT]:"2006/01/04"[PDAT]')
record = Entrez.read(handle)
print(record["Count"])
