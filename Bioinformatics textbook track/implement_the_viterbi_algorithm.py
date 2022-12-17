"""ビタビアルゴリズムは、観測された事象系列を結果として生じる隠された状態の最もらしい並び
動的計画法アルゴリズムの一種:復号化問題"""
#https://yuutookun.hatenablog.com/entry/2012/10/07/153101


file = open('/Users/kita/Downloads/rosalind_ba10c (1).txt').read()
stringx=file.split("\n")[0]#output
sigma=[i for i in file.split("\n")[2] if i!=" "] #入力するときは、スペースキーを除去してください。
states=[i for i in file.split("\n")[4] if i!=" "]#state　#入力するときは、スペースキーを除去してください。
transition=[]
for i in range(7,7+len(states)):
    transition.append([float(j) for j in file.split("\n")[i].split()[1:]])   
emission=[]
for i in range(9+len(states),9+len(states)+len(states)):
    emission.append([float(j) for j in file.split("\n")[i].split()[1:]])
    
    

def viterbi(stringx, sigma, states, transition, emission):
    initTransitionProb=1/len(states)#状態がA,B,Cだった場合、これらは等確率で現れる
    
    backtrace={}
    trace={}
    
    for i in range(len(stringx)):
        trace[i]={}
        
        if i==0:
            for current_state in states:
                trace[i][current_state]=initTransitionProb*emission[states.index(current_state)][sigma.index(stringx[i])]
        else:
            backtrace[i]={}
            for current_state in states:
                tmp_prob=-float("inf")
                for before_state in states:
                    tmp= trace[i-1][before_state]*transition[states.index(before_state)][states.index(current_state)]* emission[states.index(current_state)][sigma.index(stringx[i])]
                    if  tmp>tmp_prob:
                        trace[i][current_state]=tmp
                        tmp_prob=tmp
                        backtrace[i][current_state]=before_state
    
    #print(trace)
    #print(backtrace)
    
    current_state=max(backtrace[len(stringx)-1], key=backtrace[len(stringx)-1].get)
    hidden_path=current_state
    for i in range(len(stringx)-1,0,-1):
        before_state = backtrace[i][current_state]
        hidden_path= before_state + hidden_path
        current_state=before_state
    
    print(hidden_path)
        

    return None
        
    
viterbi(stringx, sigma, states, transition, emission)





#別解
file = open('Desktop/Downloads/rosalind_ba10c.txt').read()
stringx=file.split("\n")[0]#output
sigma=[i for i in file.split("\n")[2] if i!=" "] #入力するときは、スペースキーを除去してください。
states=[i for i in file.split("\n")[4] if i!=" "]#state　#入力するときは、スペースキーを除去してください。
transition=[]
for i in range(7,7+len(states)):
    transition.append([float(j) for j in file.split("\n")[i].split()[1:]])   
emission=[]
for i in range(9+len(states),9+len(states)+len(states)):
    emission.append([float(j) for j in file.split("\n")[i].split()[1:]])


def viterbi(stringx,sigma,states,transition,emission):
    initTransitionProb=1/len(states)#状態がA,B,Cだった場合、これらは等確率で現れる
    
    #全てのスコアを計算する
    backtrace={}
    score_dict={}#スコアを保存していく。例えば、score_dict{"A":}
    
    for i in range(0,len(stringx)):
        backtrace[i]={}
        for current_state in states:#例えば、隠れモデルがA,B,CのうちＡだった場合
            if current_state not in score_dict.keys():#もし隠れモデルがA,B,CのうちＡだった場合
                score_dict[current_state]={}#score_dict={'A':{}}と追加する
            
            if i==0: #stringxの先頭を考える時、例えば隠れモデルの先頭がＡでoutputの先頭がxだったとイメージしてみよう、
                score_dict[current_state][i]=(initTransitionProb)*(emission[states.index(current_state)][sigma.index(stringx[i])])
            else: #stringxの先頭でない時、
                score_dict[current_state][i]=-float("inf") #初期値は十分小さい値にしておく
                for state in states:#例えば、隠れモデルの前の状態がＢだったら、
                    tmp_score=(score_dict[state][i-1])*(transition[states.index(state)][states.index(current_state)])*emission[states.index(current_state)][sigma.index(stringx[i])]      #一つ前はBだったら、Aに遷移して出力がｘだった時の確率
                    
                    if tmp_score>score_dict[current_state][i]:
                        score_dict[current_state][i]=tmp_score#常に確率が高いものを選ぶ。例えば、ＢからＡに移るときスコアが最大なら、
                        backtrace[i][current_state]=state#backtraceに、i番目の現在の隠れモデルの状態Ａの前はBであると記録する
    

    max_score_state = max(score_dict.keys(), key=lambda state: score_dict[state][len(stringx) - 1])
    most_probable_path = max_score_state
    
    current_state = max_score_state
    for i in range(len(stringx)-1,0,-1):
        prev_state=backtrace[i][current_state]
        most_probable_path=prev_state+most_probable_path
        current_state=prev_state
    
    return most_probable_path

print(viterbi(stringx,sigma,states,transition,emission))





#別解
stringx="xyxzzxyxyy"

"""transition"""
AA=0.641
AB=0.359
BA=0.729
BB=0.271


"""Emission"""
Ax=0.117
Ay=0.691
Az=0.192
Bx=0.097
By=0.42
Bz=0.483


probabilities=[]
path=""

#初期
if stringx[0]=="x":
    probabilities.append((Ax,Bx))
elif stringx[0]=="y":
    probabilities.append((Ay,By))
else:
    probabilities.append((Az,Bz))

#再帰処理
for i in range(1,len(stringx)):
    lastA,lastB=probabilities[-1]
    if stringx[i]=="x":
        thisA=max(lastA*AA*Ax,lastB*BA*Ax)
        thisB=max(lastA*AB*Bx,lastB*BB*Bx)
        probabilities.append((thisA,thisB))
    elif stringx[i]=="y":
        thisA=max(lastA*AA*Ay,lastB*BA*Ay)
        thisB=max(lastA*AB*By,lastB*BB*By)
        probabilities.append((thisA,thisB))
    else:
        thisA=max(lastA*AA*Az,lastB*BA*Az)
        thisB=max(lastA*AB*Bz,lastB*BB*Bz)
        probabilities.append((thisA,thisB))

#最適状態系列の復元
for p in probabilities:
    if max(p[0],p[1])==p[0]:
        path+=("A")
    elif max(p[0],p[1])==p[1]:
        path+=("B")
        
print(path)



#勉強用資料　https://www.kabuku.co.jp/developers/hmm    
import numpy as np
    
def viterbi(stringx,sigma,states,transition,emission):
    
    #statesの種類の個数
    S = len(states) #len([A,B])==2
    
    #output_path=stringxの単語の個数
    T= len(stringx) 
    
    #累積確率の最大化を記録するための確率テーブル  (2,10)
    V = np.zeros((S,T), dtype=np.float32)
    #初期確率 AとBの初期確率は1/2ずつ
    for x in range(S):
        V[x][0]=1/S
    
    #累積確率を最大化する直前のstringxのインデックスを保持するインデックステーブル  (2,10)
    #x:0, y:1, z:2
    B = np.zeros((S,T), dtype=int)
    
    #確率テーブルV　とインデックステーブルを埋める
    for i in range(1,T):
        for j in range(S):
            V[j][i], B[j][i] = calc_table(S,T,V, i, j,stringx,sigma,transition,emission) 
            
    #テーブルを基に、各stringx中の文字について、最適なstatesを選択していく
    X= np.zeros((T), dtype=int)
    max_prob = 0.0
    for j in range(S):
        if V[j][T-1] > max_prob:
            max_prob = V[j][T-1]
            X[T-1] = j
    for i in range(T-2,0,-1):
        X[i] = B[X[i+1]][i+1]
        
    #statesのインデックスからstatesの名称(A,B)を得る
    hidden_seq=[]
    for states_idx in X:
        hidden_seq.append(states[states_idx])
        
    return "".join(hidden_seq)

#ビタビアルゴリズムの累積確率の計算処理(累積＊出力確率＊状態遷移確率)
def calc_table(S,T,V, i, j, stringx, sigma, transition, emission):
    max_prob=0.0
    max_k=0
    for k in range(S):
        # kはstate, j はcurrent state
        prob = V[k][i-1] *transition[k][j]*emission[j][sigma.index(stringx[i])] 
        
        if prob >max_prob:
            max_prob, max_k = prob, k
        
    return max_prob, max_k


print(viterbi(stringx,sigma,states,transition,emission))    
