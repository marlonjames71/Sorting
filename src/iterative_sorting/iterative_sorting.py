# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print(f"Start: {arr}")
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print(f"Index: {i}, Array = {arr}")
        # cur_index = i
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
        
        # My first attempt. You don't need a Current Index property. I don't understand why that was there to begin with. It made things a lot more confusing.
        # for j in range(i + 1, len(arr) - (cur_index + 1)):
        #     if arr[j] < arr[cur_index]:
        #         # TO-DO: swap
        #         arr[smallest_index], arr[j] = arr[j], arr[smallest_index]
        #         cur_index += 1
        #         smallest_index = j`
    return arr

# my_list3 = [7,3,8,5,11,9,4]
# my_list2 = [6,4,8,3,0,1,2,9]

# print(selection_sort(my_list2))
# print(selection_sort(my_list2))


my_nums = [5,3,8,6,7,2]
my_nums2 = [7,2,9,4,6,8,22]

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            
                
    return arr


print(bubble_sort(my_nums))
print(bubble_sort(my_nums2))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr