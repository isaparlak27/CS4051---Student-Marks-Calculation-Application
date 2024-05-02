# CS4051 Assessment Component 3 - Student Marks Calculation Application

# Program header
# Name: Student Marks Calculator
# Purpose: Calculate mean, median, and mode of entered marks
# Author: Isa Can Parlak
# Date Programmed: 19-04-2024

# Function to check if input is a number
def is_number(s):
    try:
        float(s)
        return True  # Return True if the input can be converted to a float (i.e., it's a number)
    except ValueError:
        return False  # Return False if the input cannot be converted to a float (i.e., it's not a number)

# Function to calculate mean
def calculate_mean(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    return sum(numbers) / len(numbers)  # Calculate and return the mean

# Function to calculate median
def calculate_median(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    numbers.sort()  # Sort the list of numbers
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2  # Calculate median for even number of elements
    else:
        median = numbers[n // 2]  # Calculate median for odd number of elements
    return median  # Return the calculated median

# Function to calculate mode
def calculate_mode(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty
    counts = {}  # Create a dictionary to store the frequency of each number
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1  # Increment the frequency of each number
    max_count = max(counts.values())  # Find the maximum frequency
    mode = [num for num, count in counts.items() if count == max_count]  # Find the numbers with maximum frequency
    return mode[0] if len(mode) == 1 else mode  # Return the mode (or modes) with maximum frequency

# Function to calculate skewness
def calculate_skewness(numbers):
    if len(numbers) < 3:
        return None  # Return None if less than 3 numbers are entered
    mean = calculate_mean(numbers)
    variance = sum((num - mean) ** 2 for num in numbers) / len(numbers)  # Calculate variance
    std_dev = variance ** 0.5  # Calculate standard deviation
    skewness = sum((num - mean) ** 3 for num in numbers) / (len(numbers) * std_dev ** 3)  # Calculate skewness
    return skewness  # Return the calculated skewness

# Function to read numbers from a file
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read lines from file
            numbers = []
            for line in lines:
                line_numbers = line.strip().split(',')  # Split each line by commas
                numbers.extend([float(num) for num in line_numbers if is_number(num)])  # Add numbers to the list
        return numbers
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

# Main function to run the application
def main():
    numbers = []  # Initialize an empty list to store the entered marks
    while True:
        mark = input("Enter a mark (or 'done' to finish): ")  # Prompt the user to enter a mark
        if mark.lower() == 'done':  # Check if the user entered 'done' to finish entering marks
            break  # Exit the loop if 'done' is entered
        elif ',' in mark:  # Check if the input contains commas (multiple numbers)
            numbers.extend([float(num) for num in mark.split(',') if is_number(num)])  # Add numbers to the list
        elif not is_number(mark):  # Check if the input is not a number
            print("Error: Please enter a valid number.")  # Print an error message if the input is not a number
        else:
            numbers.append(float(mark))  # Convert the input to float and add it to the numbers list

    if len(numbers) < 2:  # Check if less than 2 numbers are entered
        print("Error: Please enter at least two numbers.")  # Print an error message
        return  # Return from the main function

    print("Number of marks entered:", len(numbers))  # Print the total number of marks entered

    while True:
        print("\nMenu:")  # Print the menu options
        print("1. Print the mean of the numbers")
        print("2. Print the median of the numbers")
        print("3. Print the mode of the numbers")
        print("4. Print the skewness of the numbers")
        print("5. Enter more numbers")
        print("6. Read numbers from a file")
        print("7. Exit the application")
        choice = input("Enter your choice (1-7): ")  # Prompt the user to enter a choice from the menu

        if choice == '1':
            mean = calculate_mean(numbers)
            if mean is not None:
                print("Mean of the numbers:", mean)  # Print the calculated mean
        elif choice == '2':
            median = calculate_median(numbers)
            if median is not None:
                print("Median of the numbers:", median)  # Print the calculated median
        elif choice == '3':
            mode = calculate_mode(numbers)
            if mode is not None:
                print("Mode of the numbers:", mode)  # Print the calculated mode
        elif choice == '4':
            skewness = calculate_skewness(numbers)
            if skewness is not None:
                print("Skewness of the numbers:", skewness)  # Print the calculated skewness
        elif choice == '5':
            mark = input("Enter more numbers (separated by commas): ")
            numbers.extend([float(num) for num in mark.split(',') if is_number(num)])  # Add more numbers to the list
        elif choice == '6':
            filename = input("Enter the filename to read numbers from: ")
            numbers.extend(read_numbers_from_file(filename))  # Read numbers from file and add to the list
        elif choice == '7':
            print("Exiting the application. Goodbye!")  # Print a message and exit the application if '7' is chosen
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")  # Print an error message for invalid choices

# Calling the main function to start the program
if __name__ == "__main__":
    main()
