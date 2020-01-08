def binarySearch(searchArray, item):
    
    low=0
    high=len(searchArray)-1
    
    while low <=high:
        index=(low+high)//2
        if item ==searchArray[index]:
            return index
        elif item < searchArray[index]:
            high =index-1
        else:
            low= index +1
    
    #item hot found
    return -1
