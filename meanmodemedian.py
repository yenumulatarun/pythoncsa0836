from statistics import mean, median, mode
numbers = input("Enter the numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
