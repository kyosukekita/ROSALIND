string="""CAGCATGGTATCACAGCAGAG"""
string=string.replace(" ","")

def kmp(string):
    failure_array=[0]*len(string)
    j=failure_array[0]
    for i in range(1,len(string)):
        if string[i] !=string[j]:
            j =failure_array[j-1]
        if string[i]==string[j]:
            j+=1
        failure_array[i]=j
    return failure_array

kmp(string)



#KMP法の詳細
#https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/kmp_algorithm
#https://yottagin.com/?p=7218#

def create_table(pattern):
    table = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            table[i] = j
            j = 0
    return table

def kmp_search(string, pattern):
    table = create_table(pattern)
    i = j = 0
    while i < len(string) and j < len(pattern):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = table[j]
 
    if j == len(pattern):
        return i - j
    else:
        return None
