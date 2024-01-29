start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))
perfect_squares = []
for x in range(start_range, end_range+1):
    digit_sum = sum(int(digit) for digit in str(x))
    if int(x ** 0.5) ** 2 == x and digit_sum < 10:
        perfect_squares.append(x)

print("Numbers in the range with perfect squares and sum of digits less than 10:")
print(perfect_squares)
