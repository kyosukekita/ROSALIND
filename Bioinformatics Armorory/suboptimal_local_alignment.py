#https://github.com/erexhepa/Rosalind/blob/master/Armory_014_SUBO.py

file = open('/Users/kita/Downloads/rosalind_subo (5).txt').read()

# Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
pattern = "AAGTGAGGTAAGTAAGAAAAATGCCCTGG"


seqs=[]
for seqblock in file.split(">")[1:]:
    parts=seqblock.split("\n")
    seq_id=parts[0]
    sequence=''.join(parts[1:])
    seqs.append(sequence)
            
#print(seqs)           

def hamming_dist(string1, string2):
    return sum([x != y for x, y in zip(string1, string2)])


def count_hamming(pattern, seq, dist=3):
    """Count number of matches within dist mismatches."""
    count = 0
    pat_len = len(pattern)
    for i in range(len(seq) - pat_len + 1):
        if hamming_dist(seq[i:i + pat_len], pattern) <= dist:
            count += 1
    return count


print(count_hamming(pattern, seqs[0]), count_hamming(pattern, seqs[1]))
