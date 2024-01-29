
def sort_by_length(lst):
    return sorted(lst, key=len)


lst = input("Enter elements of the list separated by spaces: ").split()


sorted_list = sort_by_length(lst)

print("Sorted list according to the length of elements:", sorted_list)
