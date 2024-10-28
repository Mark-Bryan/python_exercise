#1
def largest_number(num1, num2, num3, num4, num5):
    biggest_number = max(num1, num2, num3, num4, num5)
    print("The largest number is: ", biggest_number)

largest_number(34, 65, 98, 134, 789)

#2
def place_words():
    character = []  

    for  i in range(5):
        word = input("Enter a word: ")
        character.append(word)  
    character.sort()
    print("The words in alphabetical order are :")
    for word in character:
        print(word)
place_words()

#3
students_grades = {
    "Blessing": 85,
    "Ryan": 90,
    "Fotsing": 78
}

average_grade = sum(students_grades.values()) / len(students_grades)


print(f"The average grade is: {average_grade}")

#4 



