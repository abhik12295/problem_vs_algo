def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    curr = 0
    p0 = 0
    p2 = len(input_list) - 1
    while curr <= p2:
        if input_list[curr] == 2:
            input_list[curr], input_list[p2] = input_list[p2], input_list[curr]
            p2 -= 1
        elif input_list[curr] == 1:
            curr += 1
        else:
            input_list[curr], input_list[p0] = input_list[p0], input_list[curr]
            p0 += 1
            curr += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Test case 3 - array with only a single element
# Should print [0]
# Should print Pass as the result array should be the same array
test_function([0])

# Test case 4 - array with empty array
# Should print Pass as the result array should also be an empty array
test_function([])