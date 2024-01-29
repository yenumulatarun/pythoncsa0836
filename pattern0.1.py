rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    print(" " * (3 * (rows - i)), end="")
    for j in range(1, i + 1):
        print(f"{j / 10:.1f}", end=" ")
    print()
