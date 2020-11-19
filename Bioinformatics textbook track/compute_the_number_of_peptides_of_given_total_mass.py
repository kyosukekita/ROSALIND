#https://byu.instructure.com/courses/3688/assignments/174302?module_item_id=312525
protein_mass_table="""
A 71 C 103 D 115
E 129 F 147 G 57
H 137 I 113 K 128
L 113 M 131 N 114
P 97 Q 128 R 156
S 87 T 101 V 99
W 186 Y 163 
"""

temp = protein_mass_table.split()
weight_list=list(set(sorted([int (k) for k in temp[1::2]])))#ロイシンとイソロイシン同じ分子量だから重複除く

m=1388

def count(weight_list,total):
    dp=[0 for _ in range(total+1)]#dp[i]は、分子量がiとなるペプチドの数
    
    for weight in weight_list:
        dp[weight]=weight_list.count(weight)
    
    for i in range(total+1):
        for weight in weight_list:
            dp[i]+=dp[i-weight]
    
    return dp[total]

count(weight_list,m)





#下の解法、は組み合わせを求めているので使えない。例えば、AAGとAGAが区別されていない?
#参考　https://qiita.com/ophhdn/items/8cb1fbe4393aee760967
coin = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]
total = 1388
def combinations(coin, total):
    dp = [int(i % coin[0] == 0) for i in range(total + 1)]
    for coin in coin[1:]:
        for i in range(coin, total+1):
            dp[i] += dp[i-coin]
    return dp[-1]

combinations(coin, total)












