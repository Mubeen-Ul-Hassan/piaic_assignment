def personal_information():
    """
    Collect user information i.e name and favourite numbers.
    """
    name = str(input("Enter your name: "))
    first_number = int(input("Enter your first favourite number: "))
    second_number = int(input("Enter your second favourite number: "))
    third_number = int(input("Enter your second favourite number: "))
    return name, first_number, second_number, third_number

def even_odd(first_number, second_number, third_number):
    """
    Return whether number is even or odd.
    """
    for number in [first_number, second_number, third_number]:
        if number % 2 == 0:
            print(f"The number {number} is even.")
        else:
            print(f"The number {number} is odd.")

def number_square(first_number, second_number, third_number): 
    """
    number_square return square of numbers
    """
    for number in [first_number, second_number, third_number]:
        print(f"The number {number} and its square: ({number, number**2})")

def number_sum(first_number, second_number, third_number):
    """
    number_sum function return sum of numbers
    """
    sum = first_number + second_number + third_number
    print(f"\nAmazing! The sum of your favourite number is: {sum}")
    return sum

def prime_number(sum): 
    """
    prime_number function return whether a number is prime  or not.
    """
    if sum > 1:
        if sum % 2 == 1:
            print(f"Wow, {sum} is a prime number!")
            return True
    return False


name, first_number, second_number, third_number = personal_information()

print(f"\nHello, {name}! Let's explore your favorite numbers:") # personalized message

even_odd(first_number, second_number, third_number)
number_square(first_number, second_number, third_number)
sum = number_sum(first_number, second_number, third_number)
prime_number(sum)