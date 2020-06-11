k=
text=""

d={}
for i in range(len(text)-k+1):
    string=text[i:i+k]
    if string[:-1] in  d.keys():
        d[string[:-1]].append(string[1:])
    else:
        d[string[:-1]]=[string[1:]]


for edge in d:
    print(edge+" -> " +','.join(d[edge]))
