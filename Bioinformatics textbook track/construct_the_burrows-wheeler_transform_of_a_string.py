#http://smrmkt.hatenablog.jp/entry/2015/01/06/002300
#https://naoya-2.hatenadiary.org/entry/20081016/1224173077

file = open('Desktop/Downloads/rosalind_ba9i.txt').read()
text=(file.split("\n")[0])


def BWT(text):
    #ソート済みの接尾辞配列を作成
    sortedArray=sorted([text[i:] for i in range(len(text))])
    #接尾辞が文字列全体と等しい場合は、文字列の最後の文字を使う
    return ''.join([text[-len(s)-1] if len(s)<len(text) else text[-1] for s in sortedArray])
    
BWT(text)
