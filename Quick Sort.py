def quicksort(arr, left, right):
    if left < right:
        
        parition_pos = parition(arr, left, right)
        quicksort(arr,left, parition_pos-1)
        quicksort(arr, parition_pos+1, right)
    
def parition(arr,left, right):
    pivot = arr[right]
    i = left
    j = right -1 
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1 
        while j > left and arr[j] >= pivot:
            j -= 1 
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]
        
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i 
    
arr = list(map(int, input("Enter your values: ").split()))
quicksort(arr, 0, len(arr)-1)
print(arr)
