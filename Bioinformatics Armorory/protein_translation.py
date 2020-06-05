from Bio.Seq import translate

s=""
translated_s=

for i in [1,2,3,4,5,6,9,10,11,12,13,14,15,16,21,22,23]:#table number
    if (translate(s,table="{}".format(i),to_stop=True))==translated_s:
        print(i)
