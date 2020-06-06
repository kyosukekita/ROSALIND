#https://www.geeksforgeeks.org/counting-inversions/

file = open('Desktop/Downloads/rosalind_inv.txt').read()
n=int(file.split("\n")[0])
A=[int(i) for i in file.split()[1:]]


def mergeSort(arr, n): 
    # A temp_arr is created to store 
    # sorted array in merge function 
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 
  
    
    
# This Function will use MergeSort to count inversions   
def _mergeSort(arr, temp_arr, left, right): 
    inv_count = 0
  
    if left < right:  
        mid = (left + right)//2
        inv_count += _mergeSort(arr, temp_arr, left, mid) 
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
    
    
# This function will merge two subarrays in a single sorted subarray 
def merge(arr, temp_arr, left, mid, right): 
    i = left     # Starting index of left subarray 
    j = mid + 1 # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray 
    inv_count = 0
  
    # Conditions are checked to make sure that i and j don't exceed their 
    # subarray limits. 
  
    while i <= mid and j <= right: 
  
        # There will be no inversion if arr[i] <= arr[j] 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array 
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
    return inv_count 


result=mergeSort(A,n)
print(result)





#遅すぎて時間オーバー
def sort(arr):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    return count
