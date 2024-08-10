"""
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.
Read the input and convert it to an integer.
Prompt the user to enter the second number.
Read the input and convert it to an integer.
Calculate the sum of the two numbers.
Print the total sum with an appropriate message.
"""

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

print(f"Total sum: {first_number + second_number}")


"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
"""

favourite_animal = str(input("What's your favourite animal? "))

if(favourite_animal):
    print(f"My favourite animal is also {favourite_animal}!")

"""
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
"""

fahrenheit_temp = int(input("Enter temperature in Fahrenheit: "))
degree_celsius = (fahrenheit_temp - 32) * 5.0 / 9.0
print(f"Temperature: {fahrenheit_temp}F = {degree_celsius}C")


"""
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
"""

first_side = int(input("What is the length of side 1? "))
second_side = int(input("What is the length of side 2? "))
third_side = float(input("What is the length of side 3? "))

print(f"The perimeter of the triangle is {first_side + second_side + third_side}")

"""
Ask the user for a number and print its square (the product of the number times itself).
"""

square_number = int(input("Type a number to see it's square: "))
print(f"{float(square_number)} squared is {float(square_number ** 2)}")

"""
Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?
"""

numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(f"3 is removed {numbers}")

"""
You have two lists:

list1 with elements [1, 2, 3]
list2 with elements [4, 5, 6].
Create a program using list method to add the elements of list2 to list1.
"""

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_2.append(list_1))