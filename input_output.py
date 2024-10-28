#1 Hello Name
name = input("Please enter your name: ")

print("Hello", name, '!')





#2 arithmetics
def numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    addition = num1 + num2
    difference = num1 - num2
    product = num1 * num2

    print(f"Sum of the two numbers is: {addition}")
    print(f"Difference between the two numbers is: {difference}")
    print(f"Product between the two numbers is: {product}")

numbers()

#3 age calculation
yearofBirth = int(input("What year were you born in?: "))

def age_calculator():
    age = 2024 - yearofBirth
    print(f"Hi there, your mom told me that you are {age} years old")
age_calculator()

#4 reverse
def reverse_string(s):
    return s[::1]
print(reverse_string("AKIKA"))

#5 Color
def favorite_color():

    color = input("What is your favorite color? ")

    print(f"Your favorite color is {color}!")

favorite_color()

#6 Concatenate
string1 = input("Enter a greeting phrase: ")
name = input("Enter your name: ")
final = string1 + name
print('Final Statement: ', final)

#7 Temperature
def celsius_to_fahrenheit():
    celsius = int(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}F")

celsius_to_fahrenheit()

#8 even or odd number

number =int(input("Please enter any number of your choice: "))

if number % 2 == 0:
    print("The number is an even number")
else:
    print("The number is an odd number")

#10 Radius of a circle

π = 3.14159
radius = int(input("Enter the radius of the circle: "))
areaOfCircle = π * radius ** 2
print("The ara of the circle is : ", areaOfCircle)
































# def is_even(num):
#     return num % 2 == 0

# print(is_even(4))  
# print(is_even(7))  

# def factorial(n):
#     if n < 0:
#         raise ValueError("Input must be a positive integer.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result


# print(factorial(5))  


# 
# def find_max(lst):
#     if not lst:
#         raise ValueError("The list is empty.")
    
#     max_value = lst[0]  # Start by assuming the first element is the largest
#     for num in lst:
#         if num > max_value:
#             max_value = num
#     return max_value

# # Example usage:
# numbers = [3, 5, 7, 2, 8, 10]
# print(find_max(numbers))  # Output: 10


# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello")) 








