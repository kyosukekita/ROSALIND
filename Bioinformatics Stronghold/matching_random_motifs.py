N=90000
GCcontent=0.6
dna="""ATAGCCGA"""

AT=dna.count("A")+dna.count("T")
GC=dna.count("G")+dna.count("C")

string_probability=((1-GCcontent)/2)**AT*(GCcontent/2)**GC
probability=1-(1-string_probability)**N
print("{:.3f}".format(probability))
