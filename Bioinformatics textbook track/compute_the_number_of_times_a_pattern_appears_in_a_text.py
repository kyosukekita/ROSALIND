text="GCGCG"
pattern="GCG"

count=0
for i in range(len(text)-len(pattern)+1):
    if pattern== text[i:i+len(pattern)]:
        count+=1
print(count)
