#Python Assignment 2

#Task 1

#We are assigned to create a gussing game with help of for loop. 

#import library
from random import randint

# Generate a random number between 1 and 50
secret_number = randint(1, 50)

# Set the number of attempts
attempts_left = 5

while attempts_left > 0:
    try:
        # Ask the user for their guess and convert it to an integer
        user_guess = int(input("Guess the secret number (between 1 and 50): "))
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} correctly!")
            break
        elif user_guess < secret_number:
            print(f"Try again! Your guess is too low. You have {attempts_left - 1} attempts left.")
        else:
            print(f"Try again! Your guess is too high. You have {attempts_left - 1} attempts left.")
        
        # Reduce the number of attempts
        attempts_left -= 1
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

# If the user runs out of attempts
if attempts_left == 0:
    print(f"Game Over! The secret number was {secret_number}. Better luck next time!")
    
# Game is ready to run!

#Task 2

def num_vowels(input_string):
    # Convert the input string to lowercase to make the counting case-insensitive
    input_string = input_string.lower()
    
    # Define a set of vowels
    vowels = set("aeiou")
    
    # Initialize a count variable to keep track of the number of vowels
    count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char in vowels:
            count += 1
    
    return count

# Test the function with the provided string
input_string = "Learning Python is fun and engaging."
result = num_vowels(input_string)
print(f"The number of vowels in the string is: {result}")

##The number of vowels in the string is: 10

#Task 3

def hours_to_min(hours):
    # Convert hours to minutes (1 hour = 60 minutes)
    minutes = hours * 60
    return minutes

# Test the function with 2.5 hours
hours_input = 2.5
result = hours_to_min(hours_input)
print(f"{hours_input} hours is equal to {result} minutes.")

#Task 4

#Converting hours into mintes

def print_multiplication_table(number):
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

# Test the function with a number, for example, 5
number_to_print = 5
print_multiplication_table(number_to_print)

#Task 5

def eligibility(age, GPA):
    # Check if the student is at least 18 years old and has a GPA of 3.0 or higher
    if age >= 18 and GPA >= 3.0:
        return True
    else:
        return False

# Test the function with different ages and GPAs 
result = eligibility(30, 3.2)  # Using positional arguments


print(result)

print("salman")

