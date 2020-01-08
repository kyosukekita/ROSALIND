array="""6 10 4 5 1 2"""
array=[int(i) for i in array.split()]
    
def insert_sort(arr):
    number=0
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] >= arr[j-1]:
                break
            else:
                (arr[j], arr[j-1]) =(arr[j-1], arr[j])
                number +=1
    return number

insert_sort(array)
