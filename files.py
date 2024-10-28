# 1
myFile = open("message.txt", 'w')
myFile.write(input("Type in your message: ")) 
myFile.close

#2


#3
def writing_names_to_file(names):
  my_names = open("names.txt", 'w')
  for name in names:
    my_names.write(name + "\n")
    print("Names written have been saved to names.txt ")

    list_of_names = ['Tancho', 'Charlie', 'Matthew', 'Sarah', 'Suhmayah']
    writing_names_to_file(list_of_names)

#4
myInfo = "My Name is Suhmayah, \n"
myInfo += "I am 18 years of age, \n"
myInfo += "My favorite color is royal blue, \n"

info = open("info.txt", 'w')
info.write(myInfo)
info.close

#5





