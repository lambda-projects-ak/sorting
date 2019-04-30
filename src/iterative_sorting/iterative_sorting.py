insert_test = [7, 6, 4, 6, 3, 2]

#   - start with the second card and insert it into the sub-array in the correct position
#   - if next card is in proper position, expand sub-array to next element
#   - when moving an item over, you have to store it in a temporary variable
# pseudo code
# for all elements from index i=1 to i = len(arr) - 1:
#   save current element @ index i in temp variable

#   loop to the left until correct position for element found
#     shift items to the right as you go
#       copy temp to correct position when found


# def insertion_sort(arr):  # loop through n-1 elements
#     for i in range(1, len(arr)):
#     temp = arr[i]
#     j = i
#     # shift left until correct position found
#     while j > 0 and temp < arr[j - 1]:
#         arr[j] = arr[j - 1]
#         j -= 1  # insert at correct position
#     arr[j] = temp

#     return arr


# def insertion_sort(arr):
#     for i in range(0, len(arr) - 1):
#         temp = arr[i]
#         for i in range(i, len(arr)):
#             if temp > arr[i]:

#             print(i)

#     print(temp)
#     print(i)
#     return arr


# print(insertion_sort(insert_test))


# TO-DO: Complete the selection_sort() function below
selection_test = [7, 6, 4, 6, 3, 2, 1, 56, 7, 12, 24, 3]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element

        # look for smallest value in array
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        print(smallest_index)
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


print(selection_sort(selection_test))

# TO-DO:  implement the Bubble Sort function below

bubble_test = [1, 5, 4, 2, 8, 6, 0]


def bubble_sort(arr):
    for j in range(len(arr)):
        swapped = False
        i = 0
        while i < len(arr) - 1:
            if arr[i] > arr[i+1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            i += 1

        if swapped == False:
            break

    return arr


print(bubble_sort(bubble_test))


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
