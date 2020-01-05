A_sequence=""""""
B_sequence=""""""

total=0
transition=0
for i in range(len(A_sequence)):
    if A_sequence[i] != B_sequence[i] :
        total +=1
        if (str(A_sequence[i]),str(B_sequence[i])) ==("A","G") or (A_sequence[i],B_sequence[i]) == ("G","A") or (A_sequence[i],B_sequence[i])==("C","T") or (A_sequence[i],B_sequence[i]) ==("T","C"):
            transition  +=1
print(transition/(total-transition))  
