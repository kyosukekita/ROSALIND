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
