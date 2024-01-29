S1 = input("Enter s1: ")
S2 = input("Enter s2: ")

if len(S1) != len(S2):
    print("Strings must have the same length")
else:
    count = sum(1 for i in range(len(S1)) if S1[i] == S2[i])
    print("Number of matching characters:", count)
