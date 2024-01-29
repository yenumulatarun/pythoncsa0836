list1 = [int(x) for x in input("Enter elements of first list separated by space: ").split()]
list2 = [int(x) for x in input("Enter elements of second list separated by space: ").split()]
merged_list = list1 + list2
sorted_list = sorted(merged_list)

print("Merged and sorted list:", sorted_list)
