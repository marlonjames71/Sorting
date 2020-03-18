# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty

    low = 0
    high = len(arr)-1
    
    # TO-DO: add missing code
    while low <= high:
        midpoint = low + high // 2
        
        if low > high:
            return -1
        
        if target < arr[midpoint]:
            high = midpoint - 1
        elif target > arr[midpoint]:
            low = midpoint + 1
        else:
            return midpoint

    return -1 # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low + high) // 2

    if len(arr) == 0:
        return -1 # array empty
    elif low > high:
        return -1
    
    # TO-DO: add missing if/else statements, recursive calls
    if arr[middle] == target:
        return middle
    elif target < arr[middle]:
        high = middle - 1
    elif target > arr[middle]:
        low = middle + 1

    return binary_search_recursive(arr, target, low, high)
