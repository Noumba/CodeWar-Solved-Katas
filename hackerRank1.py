# First challenge
import math
from ast import IsNot
from operator import mod


# my_string = "Hello, World!"

# print(my_string+"\n")
# print(range(2))
# # Second challenge

# num = int(input("Enter number: "))

# if num in range(1, 100):
#     if mod(num, 2):
#         print("Weird")
#     elif (mod(num, 2) == 0 and (num in range(2, 6))):
#         print("Not Weird")
#     elif ((mod(num, 2) == 0) and (num in range(6, 21))):
#         print("Weird even")
#     elif ((mod(num, 2) == 0) and (num > 20)):
#         print("Not Weird even")

# # 5th Challenge

# num2 = int(input())

# if num2 in range(1, 21):
#     for val in range(num2):
#         print(val**2)

# 6th challenge LeapYear
year = int(input())


def is_leap(year):
    leap = False

    if year in range(1900, (10**5)+1):
        if((mod(year, 100) == 0) and (mod(year, 400) == 0)):
            leap = not leap
        elif (year % 4 == 0) and (year % 100 != 0):
            leap = not leap
        else:
            leap = leap

    return leap


is_leap(year)
