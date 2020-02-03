string="""CAGCATGGTATCACAGCAGAG"""
string=string.replace(" ","")

def kmp(string):
    failure_array=[0]*len(string)
    j=failure_array[0]
    for i in range(1,len(string)):
        while string[i] !=string[j]:
            j =failure_array[j-1]
        if string[i]==string[j]:
            j+=1
        failure_array[i]=j
    return failure_array

kmp(string)
