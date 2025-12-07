# Data Science Assignment - Week 2
# Name: Sahil Sawant
# Python Data Structures and File Handling
# Submission Date: 07-12-2025



# Importing numpy library for Task 2
import numpy as np


# ### Task 1: Basic Operations with Arithmetic Operators

# Accepting two integers from the users
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2

# Displaying results using f-strings
print(f"\nResults of Arithmetic Operations:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {exponentiation}")


# ### Task 2 — Lists & NumPy Array Operations
# Creating a list with at least 10 numbers
numbers = [12, 45, 23, 67, 89, 34, 90, 11, 56, 78]

# Printing basic information about the list
print("Original List:", numbers)
print("Length of List:", len(numbers))
print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))

# Adding a new element and removing one element
numbers.append(100)
numbers.remove(23) 
print("\nList after add & remove operation:", numbers)

# Sorting the list in ascending order
numbers.sort()
print("Sorted List (Ascending):", numbers)

# Sorting the list in descending order
numbers.sort(reverse=True)
print("Sorted List (Descending):", numbers)

# Converting the list to a NumPy array
num_array = np.array(numbers)

# Calculating Mean, Median, and Standard Deviation

mean_value = np.mean(num_array)
median_value = np.median(num_array)
std_dev = np.std(num_array)

print("\nNumPy Array:", num_array)
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev}")


# ### Task 3: Dictionaries and Sets

# Creating a dictionary named student
student = {
    "name": "Sahil",
    "age": 23,
    "course": "Data Science",
    "marks": 82
}

# Printing key-value pairs using a loop
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Adding a new key to the dictionary
student["grade"] = "A"
print("\nAfter Adding Grade:", student)

# Creating a set of unique courses
courses_set = {"Python", "Data Science", "AI", "Python"}  # 'Python' appears twice but set will keep unique values
print("\nUnique Courses Set:", courses_set)

# Performing set operations
set1 = {"Python", "AI", "ML"}
set2 = {"Data Science", "AI", "Python"}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print("\nSet Operations:")
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (set1 - set2):", difference_set)


# ### Task 4: File Handling

# Create and write student data into file
with open("student_data.txt", "w") as file:
    file.write("Sahil, Data Science, 85\n")
    file.write("Priya, AI, 72\n")
    file.write("Rohan, Python, 90\n")
    file.write("Meera, Machine Learning, 78\n")
    file.write("Amit, Data Analytics, 65\n")

print("Data written successfully to student_data.txt")

# Read the file and display only students with marks above 75
print("\nStudents with marks above 75:")
with open("student_data.txt", "r") as file:
    for line in file:
        name, course, marks = line.strip().split(", ")
        if int(marks) > 75:
            print(f"Name: {name} | Course: {course} | Marks: {marks}")