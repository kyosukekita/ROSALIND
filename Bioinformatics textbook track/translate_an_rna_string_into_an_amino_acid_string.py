sequence="""ACCGGGGG"""
codon=[sequence[i:i+3] for i in range(0,len(sequence),3)]


def translate(x):
    if x=="UUU"or x=="UUC":
        return "F"
    elif x=="UUA"or x=="UUG"or x=="CUU"or x=="CUC"or x=="CUA"or x=="CUG":
        return "L"
    elif x=="AUU"or x=="AUC" or x=="AUA":
        return "I"
    elif x=="AUG":
        return "M"
    elif x=="GUU"or x=="GUC"or x=="GUA"or x=="GUG":
        return "V"
    elif x=="UCU"or x=="UCC"or x=="UCA"or x=="UCG":
        return "S"
    elif x=="CCU"or x=="CCC"or x=="CCA"or x=="CCG":
        return "P"
    elif x=="ACU"or x=="ACC"or x=="ACA"or x=="ACG":
        return "T"
    elif x=="GCU"or x=="GCG"or x=="GCA"or x=="GCC":
        return "A"
    elif x=="UAU"or x=="UAC":
        return "Y"
    elif x=="CAU"or x=="CAC":
        return "H"
    elif x=="CAA"or x=="CAG":
        return "Q"
    elif x=="AAU"or x=="AAC":
        return "N"
    elif x=="AAA"or x=="AAG":
        return "K"
    elif x=="GAU"or x=="GAC":
        return "D"
    elif x=="GAA"or x=="GAG":
        return "E"
    elif x=="UGU"or x=="UGC":
        return "C"
    elif x=="UGG":
        return "W"
    elif x=="CGU"or x=="CGA"or x=="CGC"or x=="CGG"or x=="AGA"or x=="AGG":
        return "R"
    elif x=="AGU"or x=="AGC":
        return "S"
    elif x=="GGU"or x=="GGC"or x=="GGA"or x=="GGG":
        return "G"
    elif x=="UGA" or x=="UAA" or x=="UAG":
        return ""
    else:
        return "-"

print("".join([translate(x) for x in codon]))
