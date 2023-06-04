def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        mergesort(left_array)
        mergesort(right_array)
        left_array_index = 0
        right_array_index = 0
        merged_array_index = 0

        while left_array_index < len(left_array) and right_array_index < len(right_array):
            if left_array[left_array_index] <= right_array[right_array_index]:
                array[merged_array_index] = left_array[left_array_index]
                left_array_index += 1
            else:
                array[merged_array_index] = right_array[right_array_index]
                right_array_index += 1
            merged_array_index += 1

        while left_array_index < len(left_array):
            array[merged_array_index] = left_array[left_array_index]
            left_array_index += 1
            merged_array_index += 1

        while right_array_index < len(right_array):
            array[merged_array_index] = right_array[right_array_index]
            right_array_index += 1
            merged_array_index += 1


