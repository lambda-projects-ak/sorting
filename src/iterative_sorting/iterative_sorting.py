test = [7, 6, 4, 6, 3, 2, 1, 56, 7, 12, 24, 3]


#   - start with the second card and insert it into the sub-array in the correct position
#   - if next card is in proper position, expand sub-array to next element
#   - when moving an item over, you have to store it in a temporary variable

# def insertion_sort(arr):
#     for i in range(0, len(arr)):
#         print(i)

#     return arr


# print(insertion_sort(test))


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element

        # look for smallest value in array
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        print(smallest_index)
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


print(selection_sort(test))

# TO-DO:  implement the Bubble Sort function below

bubble_test = [1, 5, 4, 2, 8, 6, 0, 3, 7, 9]


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(bubble_test))

# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
