def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2
        # check mid
        if input_list[mid] == number:
            return mid
        # check in left part
        if input_list[left] <= input_list[mid]:
            if number > input_list[mid] or number < input_list[left]:
                # shift left pointer to right part
                left = mid + 1
            else:
                right = mid - 1
        # check in right part
        else:
            if number > input_list[mid] or number < input_list[right]:
                # shift right pointer to left part
                right = mid - 1
            else:
                left = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# array with non-rotated arrays
test_function([[1, 2, 3, 4], 3])
# Empty array, should return -1
test_function([[], 5])
# without target value
test_function([[6, 7, 8, 1, 2, 3, 4], 5])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
