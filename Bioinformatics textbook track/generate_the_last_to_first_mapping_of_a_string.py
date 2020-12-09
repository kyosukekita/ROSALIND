#http://smrmkt.hatenablog.jp/entry/2015/01/06/002300
#https://naoya-2.hatenadiary.org/entry/20081016/1224173077

file = open('Desktop/Downloads/rosalind_ba9k.txt').read()
transform=(file.split("\n")[0])
i=int(file.split("\n")[1])


def last_to_first(text,i):
    first = [x for x in range(len(text))]
    first = sorted(first, key=lambda x: text[x])
    output = ""
    
    idx = text.index('$')
    for _ in range(len(text)):
        before=idx
        idx = first[idx]
        if idx==i:
            return before
    
    
print(inv_BWT(transform,i))
