#introduction_to_pattern_matching.pyと同じ解法

class Trie( object):
    def __init__(self):
        self.count=1 #number of nodes
        self.root=[self.count, {}] #[1、{}]
    
    def insert(self, sequence):
        node=self.root #[1、{}]
        for base in string:
            if base not in node[1]:
                self.count =self.count+1
                node[1][base]=[self.count,{}] #[1、{A：[2、{}]}]
            node=node[1][base] #[2、{}]


def recursive_format(node):
    for base, node2 in node[1].items():
        print(str(node[0]-1)+"->"+str(node2[0]-1)+":"+base)
        recursive_format(node2)

if __name__== '__main__':
    entry=open('Desktop/Downloads/rosalind_ba9a.txt').readlines() 
    #readlinesはファイルの内容を全て読み出し1行ごとのリストにする。
    data=[]
    
    for line in entry:
        data.append(line.strip())#空白文字(スペースやタブ、改行)を削除する
   
    trie_sequences= Trie()
    
    for string in data:
        trie_sequences.insert(string)


    recursive_format(trie_sequences.root)
