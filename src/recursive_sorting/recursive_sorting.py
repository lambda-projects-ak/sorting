# TO-DO: complete the helper function below to merge 2 sorted arrays

ms_data = [6, 1, 2, 8, 4, 3, 2, 1, 6, 8, 1]


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    ia = 0
    ib = 0

    for i in range(0, len(merged_arr)):
        if len(arrA) <= ia:
            merged_arr[i] = arrB[ib]
            ib += 1
        elif len(arrB) <= ib:
            merged_arr[i] = arrA[ia]
            ia += 1
        elif arrA[ia] > arrB[ib]:
            merged_arr[i] = arrB[ib]
            ib += 1
        else:
            merged_arr[i] = arrA[ia]
            ia += 1

        print(merged_arr)

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        left = merge_sort(arr[: (len(arr) // 2)])
        right = merge_sort(arr[(len(arr) // 2):])
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
