# QUICKSORT ALGORITHM
# quick_sort([12, 7, 10, 9, 11])
# pivot_index = partition([12, 7, 10, 9, 11], 0, 4)
# pivot = 11, i = -1
# [7, 10, 9, 12, 11]
# [7, 10, 9, 11, 12], i = 2
# pivot_index = 3
# quick_sort([7, 10, 9, 11, 12], 0, 2)
# pivot = arr[2] = 9, i = -1
# [7, 10, 9, 11, 12]
# [7, 9, 10, 11, 12], i = 1
# pivot_index = 2
# quick_sort([7, 9, 10, 11, 12], 0, 1)
# pivot = arr[1] = 9, i = -1
# [7, 9, 10, 11, 12] 
# [7, 9, 10, 11, 12], i = 0
# pivot_index = 1
# quick_sort([7, 9, 10, 11, 12], 0, 0)
# return [7, 9, 10, 11, 12]
# ... (right sorting)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

# Exemplo de uso:
arr = [12, 7, 10, 9, 11]
print(quicksort(arr, 0, len(arr) - 1))
