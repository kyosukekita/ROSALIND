#http://smrmkt.hatenablog.jp/entry/2015/01/06/002300
#https://naoya-2.hatenadiary.org/entry/20081016/1224173077

file = open('Desktop/Downloads/rosalind_ba9j (1).txt').read()
transform=(file.split("\n")[0])


def inv_BWT(text):
    #終端文字の位置を取得
    p=text.index('$')
    #各文字の出現回数をカウント
    count={s:text.count(s) for s in set(list(text))}
    #辞書順に並べたときの,各文字より前にある文字の合計個数を算出
    #LFマッピングの右辺第2項を出すのに必要
    
    total=0
    for k in sorted(count):
        cur=count[k]
        count[k] =total
        total+=cur
    
    #LFのマッピングを行う
    lf_mapping=[text[:i+1].count(text[i])+count[text[i]]-1 for i in range(len(text))]
    #終端文字から逆順にたどる
    ret=""
    for i in range(len(text)-1):
        ret=text[lf_mapping[p]]+ret
        p=lf_mapping[p]
    
    return ret+"$"
    
print(inv_BWT(transform))





file = open('Desktop/Downloads/rosalind_ba9j.txt').read()
transform=(file.split("\n")[0])
i=int(file.split("\n")[1])


def inv_BWT(text):
    array = [x for x in range(len(text))]
    array = sorted(array, key=lambda x: text[x])
    output = ""
    
    idx = text.index('$')
    for _ in range(len(text)):
        idx=array[idx]
        output+=text[idx]
    
    return output
    
    
print(inv_BWT(transform))
