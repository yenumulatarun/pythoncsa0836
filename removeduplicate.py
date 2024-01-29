def remove_duplicates(arr):
    if not arr:
        return []
    result = [arr[0]]
    for num in arr[1:]:
        if num != result[-1]:
            result.append(num)
    return result
user_input = input("Enter sorted array elements separated by spaces: ")
sorted_array = list(map(int, user_input.split()))
unique_array = remove_duplicates(sorted_array)
print("Array after removing duplicates:", unique_array)
