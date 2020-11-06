file= open('Desktop/Downloads/rosalind_ba3h.txt').read()#ファイルの一番下の空行消す
k=int(file.split("\n")[0])
strings=file.split("\n")[1:]

def main(strings):
    
    tmp={}
    for string in strings:
        tmp[string[:-1]]=string[1:]
    
    
    pattern_answer=""
    for i in range(len(strings)):
        pattern=""
        root=strings[i][:-1]　#スタートとなるノードを全て試して、↓
        child=root
        pattern+=child
        while True:
            child=tmp[child]
            pattern+=child[-1]
            if child not in tmp:
                break
        
        if len(pattern_answer) < len(pattern): #パターンの長さが一番長くなったものを選ぶ
            pattern_answer=pattern
            
        
    print(pattern_answer)

    
main(strings)
