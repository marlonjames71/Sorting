# TO-DO: complete the helpe function below to merge 2 sorted arrays

# -------------------------------------------------------------------------

# Think of recursion by solving the smallest  relevant/full problem
# [4, 7, 3, 1]

# [4] [7] [3] [1]

# [4, 7] [1, 3]

#  i
# [4 7]
# [1 3]
#  j

# -------------------------------------------------------------------------

# [7, 4, 8, 1, 2, 9, 3]

# [7, 4, 8] [1, 2, 9, 3]

# [7] [4, 8] [1, 2] [1, 2] [9, 3]

# [7] [] [4] [8] [1] [2] [9] [3]

# [7] [4, 8] [1, 2] [3, 9] 

# [4, 7, 8] [1, 2, 3, 9]

# [1, 2, 3, 4, 7, 8, 9]

#         i
# a [ 4 7 8 ]
# b [ 1 2 3 9 ]
#           k 


# TO-DO: Complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Given 2 arrays
    # Combine into sorted array
    a = 0
    b = 0
    
    for i in range(0, elements):
        # if a is done
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
            
        # if b is done
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
            
        # if a is smaller
        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
            
        # if b is smaller
        else:
            merged_arr[i] = arrB[b]
            b += 1
    # Do this by...
    
    # Compare the first element of each
    
    # Add the smallest to the merged array
    
    # Iterate the pointer for the smaller value
    
    # If one pointer reaches the end of it's array
    # Push all the remaining values in the other array to the end of merged
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# This function also handles the divide part
def merge_sort( arr ):
    # Base case: arr length 0 or 1
    if len(arr) > 1:
        
    # Otherwise
    # Find the middle of array with // 2
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 :])
    # Divide to left and right ()
    # Do merge sort on left and right (because this firther divides)
    
    # Put it back together by merging left and right
        arr = merge(left, right)
    

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
