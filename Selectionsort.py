def selectionsort(arr):
    if len(arr) > 1:
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:  
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]


test_arr = [1, 5, 4, 2, 0]
selectionsort(test_arr)
print(test_arr)
