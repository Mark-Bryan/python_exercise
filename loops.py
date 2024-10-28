#1
for i in range(1, 50):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Bizz")


#2




#3
number = int(input('Any Number: '))

is_prime = True
for num in range(2, number):
    if(number) % num == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#4



#5


#6
for num in range(1, 100):
    if num % 2 == 0:
        print(num)