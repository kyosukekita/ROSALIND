nucleotide={"A":"00","C":"01","G":"10","T":"11"}

def patternToNumber(pattern):
    number="0b"#先頭に0bを付けることで二進数
    for i in range(len(pattern)):
        number += nucleotide[pattern[i]]
    print(int(number,2))#2進数で表示

patternToNumber("AGT")
