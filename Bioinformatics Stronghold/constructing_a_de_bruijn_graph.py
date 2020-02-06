strings= open('Desktop/Downloads/sample3.txt').read()

def reverse_complement(sequence):
    temp=sequence.replace("A","X").replace("T","A").replace("X","T")
    return (temp.replace("G","X").replace("C","G").replace("X","C")[::-1])

S=strings.split('\n')
Src=list(map(reverse_complement,S))
Stotal=set(S+Src)
Stotal=list(Stotal)

for i in Stotal:
    print("(" + i[:-1] + ", " + i[1:] + ")")
