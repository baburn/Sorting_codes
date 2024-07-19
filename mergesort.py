def mergesort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        mergesort(left_arr)
        mergesort(right_arr)
        
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1 
                
            k += 1 
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1 
            k += 1 
            
        while j < len(right_arr):
            arr[k] =  right_arr[j]
            j += 1 
            k += 1 
            
arr_test = [5, 3, 13, 11, 75, 69, 63, 4]
mergesort(arr_test)
print(arr_test)