
ms_data = [1, 6, 2, 8, 2, 4]


# def split_array(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         print(left)
#         split_array(left)
#         print(right)
#         split_array(right)


data_1 = [1, 2, 3]
data_2 = [4, 5, 6]

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    for i in merged_arr:
      # make sure to pop item from list as you go or keep track of what element you are looking at
        if arrA[i] < arrB[i]:
            # all elements in arrA have been merged, put next element in arrB into merged array
            merged_arr.insert(arrA[i], i)
        elif False:
            # all elements in arrB have been merged, put next element in arrA into merged array
            pass
        elif False:
            # next element in arrA smaller, add to merged array
            pass
        else:
            # next element in arrB smaller, add to merged array
            pass

    return merged_arr


# print(merge(data_1, data_2))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # [1, 6, 2, 8, 2, 4]
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        # [1, 6, 2]
        # [1]
        # [6, 2]
        # [6]
        # [2]
        # [8, 2, 4]
        # [8]
        # [2, 4]
        # [2]
        # [4]
        arr = merge(left, right)

    return arr


print(merge_sort(ms_data))


#
#
#
#
#
#
#
#
#
#

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
