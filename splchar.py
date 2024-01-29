string = input("Enter a string: ")
words = string.split()
count = sum(1 for word in words if word.startswith('T'))

print("Number of words starting with 'T':", count)
