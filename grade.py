# Function to calculate the grade based on marks
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

# Take user input for the number of subjects
while True:
    try:
        num_subjects = int(input("Enter the number of subjects: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

total_marks = 0

# Calculate total marks and average marks
for i in range(num_subjects):
    while True:
        try:
            marks = float(input(f"Enter the marks of subject {i+1}: "))
            break
        except ValueError:
            print("Please enter a valid floating-point number.")

    total_marks += marks

average_marks = total_marks / num_subjects

# Calculate grade based on average marks
grade = calculate_grade(average_marks)

# Print average marks and grade
print(f"Average marks: {average_marks}")
print(f"Grade: {grade}")
