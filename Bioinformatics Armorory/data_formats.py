from Bio import Entrez
Entrez.email="myemail.com"
handle = Entrez.efetch(db="nucleotide", id=["NM_001271262, JF927165, JX462666, NM_000641, JF927157, JQ011270, NM_013179, JX308803"], rettype="fasta")
records = handle.read()
print(records)
