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
