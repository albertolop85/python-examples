
def quick_sort(arr, begin, end) :
    
    if begin < end :

        partitionIndex = partition(arr, begin, end)
        quick_sort(arr, begin, partitionIndex - 1)
        quick_sort(arr, partitionIndex + 1, end)


def partition(arr, begin, end) :
    
    pivot = arr[end]
    i = begin

    print (arr)

    for j in range(begin, end) :
        
        if (arr[j] <= pivot) :
            
            swap = arr[i]
            arr[i] = arr[j]
            arr[j] = swap

            i = i + 1
        
        j = j + 1
    
    swap = arr[i]
    arr[i] = arr[end]
    arr[end] = swap

    return i



array = [34, 23, 22, 89, 76, 54, 91, 8, 45, 17]

print (array)

quick_sort(array, 0, len(array) - 1)

print (array)