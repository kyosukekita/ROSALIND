file=open('Desktop/Downloads/rosalind_ba9b.txt').read()
text=file.split("\n")[0]
strings=[i for i in file.split("\n")[1:] if i!=""]

#construct a trie from patterns

class Trie(object):
    def __init__(self):
        self.count=0 #number of nodes
        self.root=[self.count, {}] #[1、{}]
    
    def insert(self, sequence):
        node=self.root #[1、{}]
        for base in sequence:
            if base not in node[1]:
                self.count =self.count+1
                node[1][base]=[self.count,{}] #[1、{A：[2、{}]}]
            node=node[1][base] #[2、{}]

t= Trie()
for string in strings:
    t.insert(string)
    
    
#prefixTrieMAtching
def prefixTrieMatching(text,Trie):
    k=0
    symbol=text[k]#first letter of text
    v=Trie.root#root of Trie [0, {'A': [1, {'T': [2, {'C': [3, {'G': [4, {}]}]}]}], 'G': [5, {'G': [6, {'G': [7, {'T': [8, {}]}]}]}]}]
    
    while k<len(text)-1:
        if v[1] =={}:#if v is a leaf in Trie
            return True
        elif symbol in v[1]:#else if there is an dege(v,w) in Trie labeld by symbol
            v=v[1][symbol]
            k+=1
            symbol=text[k]#next letter of text 
        else:
            return False
    
    return False


answer=[]
for i in range(len(text)-len(strings[0])+1):#ここはスマートではない。patternの長さより大きいものは探索しなくてよい、という原理
    subtext=text[i:]
    if prefixTrieMatching(subtext,t):
        answer.append(i)
        
print(" ".join(map(str,answer)))
