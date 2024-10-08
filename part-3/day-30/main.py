#FileNotFound
# with open("a_file.txt") as file:
#     file.read()
# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")


bmi = weight / (height * height)
print(bmi)


#KeyError
#a_dictionary = {"key":"value"}
#value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "poo", "pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)