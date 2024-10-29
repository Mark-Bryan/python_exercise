#1 Hello Name
name = input("Please enter your name: ")

print("Hello", name, '!')


#2 arithmetics
def numbers():
    num1 = int(input("Enter the first number(Only integers please): "))
    num2 = int(input("Enter the second number(Only integers please): "))

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
print(reverse_string("LA MASIA"))

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
print("The area of the circle is : ", areaOfCircle)









