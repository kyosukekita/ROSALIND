#https://www.youtube.com/watch?v=LB-ANFydv30
#http://www.nct9.ne.jp/m_hiroi/light/pyalgo57.html
#https://rosettacode.org/wiki/Suffix_tree#Python　今回用いたのは←のコード

#https://www.geeksforgeeks.org/suffix-tree-application-3-longest-repeated-substring/

class Node:
    def __init__(self, sub="", children=None):
        self.sub=sub #全てのエッジは空ではないsubstringによってラベル付けされる
        self.ch=children or [] #子ノードの番号


class SuffixTree:
    def __init__(self,str):#文字を渡してsuffixを次々と追加していく
        self.nodes=[Node()]
        for i in range(len(str)):
            self.addSuffix(str[i:])
    
    
    def addSuffix(self,suf):
        n=0#今見ているノードの番号
        i=0#今見ているsuffixの文字の場所
        while i<len(suf):
            b=suf[i]# suffixの中で、注目している文字をbとする
            x=0
            while True:
                children=self.nodes[n].ch #今注目しているノードの子供
                if len(children)==x: #今注目しているノードの子供の個数とｘが等しければ、
                    #no matching child, remainder of suf becomes new node
                    n1=len(self.nodes) #既に登録しているnodeの個数==n+1番目の数字
                    self.nodes.append(Node(suf[i:],[])) #今注目しているノードに、「suffixのi番目以降の文字」と「空の子供」を登録し、
                    self.nodes[n].ch.append(n1) #ノードnの子供にn+1番の数字を登録する
                    return
                n1=children[x] #今注目しているノードの子供のx番目のノードの番号
                if self.nodes[n1].sub[0]==b:
                    #もしも「注目しているノードのsubstringの開始の文字」が、「suffixの中で、注目している文字b」と等しければ、
                    break #抜ける
                x +=1 #xを一つ進める
            
            #find prefix of remaining suffix in common with child
            sub1=self.nodes[n1].sub
            j=0
            while j< len(sub1):
                if suf[i+j]!=sub1[j]:
                    #spilt n1
                    n2=n1
                    #new node for the past in common
                    n1=len(self.nodes)#既に登録しているnodeの個数
                    self.nodes.append(Node(sub2[:j],[n2]))
                    self.nodes[n2].sub=sub2[j:] #old node loses the part in common
                    self.nodes[n].ch[x1]=n1
                    break
                j+=1
            i+=j
            n=n1#continue down the tree
    
    def print(self):
        for i in range(1,len(self.nodes)):
            print(self.nodes[i].sub)
                    
                
                    
text="ATAAATG$"
s=SuffixTree(text)
s.print()
