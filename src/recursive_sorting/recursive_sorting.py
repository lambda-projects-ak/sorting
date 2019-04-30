
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

ms_data = [1, 6, 2, 8, 2, 4, 7, 3, 5, 9, 6]


def split_array(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        print(left)
        print(right)
        split_array(left)
        split_array(right)


split_array(ms_data)


data_1 = [1, 2, 3]
data_2 = [4, 5, 6]

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
        # elements = len(arrA) + len(arrB)
        # merged_arr = [0] * elements
        # TO-DO
    merged_arr = arrA + arrB

    return merged_arr


# print(merge(data_1, data_2))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


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
