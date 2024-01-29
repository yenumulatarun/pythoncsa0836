string1 = input("Enter the first string: ").replace(" ", "").lower()
string2 = input("Enter the second string: ").replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
