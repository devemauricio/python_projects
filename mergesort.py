 
# [3, 1, 5, 4]
# left = [3,1], right = [5,4]
# left_sorted([3,1])
#   left = [3], right = [1]
#   left_sorted([3]) = [3]
#   right_sorted([1]) = [1]
#   return merge([3], [1]) => [1, 3]
# left_sorted = [1,3]

# right_sorted([5, 4])
#   left = [5], right = [4]
#   left_sorted([5]) = [5]
#   right_sorted([4]) = [4]
#   merge([5], [4]) => return [4, 5]
# right_sorted = [4, 5]

# return merged([1,3], [4,5]) => [1,3,4,5]

def merge(left,right):
    i, j = 0, 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    lst += left[i:]
    lst += right[j:]
    return lst
  
def mergesort(arr):
    if len(arr) == 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    
    return merge(left_sorted, right_sorted)

arr = [3, 1, 5, 4]
print(mergesort(arr))
