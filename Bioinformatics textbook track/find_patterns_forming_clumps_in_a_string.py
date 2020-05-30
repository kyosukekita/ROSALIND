genome=""
k=9
L=537
t=16


answer=set()
for i in range(len(genome)-L+1):
    subseq=genome[i:i+L]
    for j in range(len(subseq)-k+1):
        if subseq.count(subseq[j:j+k])==t:
            answer.add(subseq[j:j+k])

print(' '.join(answer))
