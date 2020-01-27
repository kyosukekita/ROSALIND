#used https://github.com/mtarbit/Rosalind-Problems/blob/master/e025-long.py as a reference

file = open('Desktop/Downloads/rosalind_long.txt').read()

sequence_list=[]
for seqblock in file.split(">")[1:]:
    parts = seqblock.split("\n")
    seq = ''.join(parts[1:])
    sequence_list.append(seq)

def genome_assembler(arr, genome=''):
    if len(genome)==0:
        genome = arr.pop(0)
        return genome_assembler(arr,genome)
    
    else:
        for i in range(len(arr)): 
            a=arr[i]
            l = len(a)
            for p in range(int(l/2)):
                q = l - p
                if genome.startswith(a[p:]):
                    del arr[i]
                    return genome_assembler(arr,genome= a[:p] + genome)
                if genome.endswith(a[:q]):
                    del arr[i]
                    return genome_assembler(arr,genome= genome + a[q:])
        return genome

print(genome_assembler(sequence_list))
