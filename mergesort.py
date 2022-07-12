
def merge_sort(arr, n) :
    
    if n < 2 :
        return
    
    mid = int(n / 2)
    left = [None] * mid
    right = [None] * (n-mid)

    for i in range(0, mid) :
        left[i] = arr[i]
        i = i + 1
    
    for i in range(mid, n) :
        right[i-mid] = arr[i]
        i = i + n

    merge_sort(left, mid)
    merge_sort(right, n - mid)
    
    merge(arr, left, right, mid, n - mid)


def merge(arr, left, right, leftSize, rightSize) :

    i = 0
    j = 0
    k = 0

    while i < leftSize and j < rightSize :

        if left[i] <= right[j] :
            arr[k] = left[i]
            i = i + 1
        else :
            arr[k] = right[j]
            j = j + 1

        k = k + 1
    
    while i < leftSize :
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    
    while j < rightSize :
        arr[k] = right[j]
        j = j + 1
        k = k + 1


array = [34, 23, 22, 89, 76, 54, 91, 8, 45, 17]

print (array)

merge_sort(array, len(array))

print (array)