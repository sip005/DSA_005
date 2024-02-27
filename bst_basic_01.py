def binary_search(ordered_list: list, target: int):
    
    size_of_the_list = len(ordered_list) - 1
    
    index_of_first_element = 0
    index_of_last_element = size_of_the_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element) // 2

        if ordered_list[mid_point] == target:
            return mid_point
        elif ordered_list[mid_point] < target:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1

    return None

# Test Case 1: Basic case with a target in the middle
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(input_list, target)
print(result)  # Expected output: 4

# Test Case 2: Target at the beginning of the list
input_list = [10, 20, 30, 40, 50]
target = 10
result = binary_search(input_list, target)
print(result)  # Expected output: 0

# Test Case 3: Target at the end of the list
input_list = [10, 20, 30, 40, 50]
target = 50
result = binary_search(input_list, target)
print(result)  # Expected output: 4

# Test Case 4: Target not in the list
input_list = [10, 20, 30, 40, 50]
target = 25
result = binary_search(input_list, target)
print(result)  # Expected output: None

# Test Case 5: Empty list
input_list = []
target = 42
result = binary_search(input_list, target)
print(result)  # Expected output: None
