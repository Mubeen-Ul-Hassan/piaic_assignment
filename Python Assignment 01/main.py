
"""
Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.
"""


friends_age = {
    "Anton": 3,
    "Beth": 6,
    "Chen": 5,
    "Drew": 6,
    "Ethan": 7
}

for key, value in friends_age.items():
    print(f"{key} is {value}.")


"""
Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
"""

name:str = "Alice"
age:int = 30
city:str = "New York"


print(f"{name} is {age} years old and lives in {city}.")


"""
Task: Given the string s, use string methods to:
Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
Convert to uppercase: change all characters in the string to uppercase.
Convert to lowercase: change all characters in the string to lowercase.
"""

s:str = "hElLo WoRlD"

print(f"Capitalize: {s[0].upper() + s[1::].lower()}")
print(f"Uppercase: {s.upper()}")
print(f"Lowercase: {s.lower()}")


"""
Task: Given the string s, use string methods to:
Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
"""

s:str ="the quick brown fox jumps over the lazy dog"

print(f"index of 'fox' is {s.find('fox')}")
print(f"'the' appears {s.count('the')}")

"""
Task: Given the string s, use string methods to:
Replace "Python" with "Java": substitute "Python" with "Java".
"""

s:str ="I love programming in Python"

print(s.replace("Python","Java"))


"""
Task: Given the string s, use string methods to:
Split into a list: break the string into a list of substrings based on the delimiter ,.
Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.
"""

s:str ="apple,banana,cherry,dates"

print(s.split(","))
print("".join(s))


"""
Task: Given the string s, use string methods to:
Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
"""

s:str ="   Python is fun!   "

print(s.strip())
print(s.strip() + "*"*5)
print("*"*5 + s.strip())

"""
Task: Given an integer num
Obtain the binary representation of num
"""

num:int = 45

print(bin(num))

"""
Task: Given two integers base and exponent
Compute base raised to the power of exponent.
"""

base:int = 3
exponent:int = 4

print(f"Power result: {base**exponent}")

"""
Task: Given a floating-point number value
Round value to the nearest integer.
Round value to two decimal places.
"""

value:float = 12.34567

print(f"Rounded to nearest integer: {round(value)}")
print(f"Rounded to two decimal places: {round(value, 2)}")