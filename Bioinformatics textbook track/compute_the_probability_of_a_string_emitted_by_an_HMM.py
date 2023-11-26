file = open('/Users/kita/Downloads/rosalind_ba10d (1).txt').read()
string=file.split("\n")[0]#output
sigma=[i for i in file.split("\n")[2] if i!="	"] #入力するときは、スペースキーを除去してください。
states=[i for i in file.split("\n")[4] if i!="	"]#state　#入力するときは、スペースキーを除去してください。
transition=[]
for i in range(7,7+len(states)):
    transition.append([float(j) for j in file.split("\n")[i].split()[1:]])   
emission=[]
for i in range(9+len(states),9+len(states)+len(states)):
    emission.append([float(j) for j in file.split("\n")[i].split()[1:]])
    
    
#前回のviterbiアルゴリズムを少し改変
prob=1/len(states)
history=[{} for _ in range(len(string))]
#history=[{"A":0.5, "B":0.5}, {"A":0.3, "B":0.4]] history[i]のAが0.3とは、pathがi番目の時にAになっている確率の最大が0.3
backtrace=[{} for _ in range(len(string))]
#backtrace=[{"A":"A", "B":"A"},{"A":"B","B":"A"}] backgrace[i]のAがAとは、pathがi番目の時にAになっている確率の最大がAの時、A→Aの遷移が起こったということ

#初期設定
for i in range(len(states)):
    history[0][states[i]]=prob*emission[i][sigma.index(string[0])]# history=[{"A":0.5*Ax, "B":0.5*Bx}]

for i in range(1,len(string)):
    for j in range(len(states)):
        register=0
        for k in range(len(states)):
            tra=transition[k][j]#history[i-1]["A"] or  history[i-1]["B"]→history[i]["A"] に遷移
            emi=emission[j][sigma.index(string[i])]#A(i)→x(i)を出力           
            
            tmp = history[i-1][states[k]]*tra*emi
            
            register +=tmp#改変箇所←全てのtmpを合計した。
        history[i][states[j]]=register

sum(history[-1].values())


#ビタビアルゴリズムのコードを少し改変
file = open('Desktop/Downloads/rosalind_ba10d (2).txt').read()
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
    score_dict={}#スコアを保存していく。例えば、score_dict{"A":}
    
    for i in range(0,len(stringx)):
        for current_state in states:#例えば、隠れモデルがA,B,CのうちＡだった場合
            if current_state not in score_dict.keys():#もし隠れモデルがA,B,CのうちＡだった場合
                score_dict[current_state]={}#score_dict={'A':{}}と追加する
            
            if i==0: #stringxの先頭を考える時、例えば隠れモデルの先頭がＡでoutputの先頭がxだったとイメージしてみよう、
                score_dict[current_state][i]=(initTransitionProb)*(emission[states.index(current_state)][sigma.index(stringx[i])])
            else: #stringxの先頭でない時、
                score_dict[current_state][i]=0 #初期値は0
                for state in states:#例えば、隠れモデルの前の状態がＢだったら、
                    tmp_score=(score_dict[state][i-1])*(transition[states.index(state)][states.index(current_state)])*emission[states.index(current_state)][sigma.index(stringx[i])]      #一つ前はBだったら、Aに遷移して出力がｘだった時の確率
                    score_dict[current_state][i]+=tmp_score#隠れモデルのi番目がcurrent_stateとなる確率を合計していく。
                        
    #Ascore=list(score_dict['A'].values())
    #Bscore=list(score_dict['B'].values())
    
    probability=0
    for state in states:
        probability+=list(score_dict[state].values())[-1]
    
    return probability
    


print(viterbi(stringx,sigma,states,transition,emission))
