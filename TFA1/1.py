f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = input("Enter your age : ")

full_name = f_name + " " + l_name

sliced_name = f_name[:3]

greet = "Hello, {}! Welcome. You are {} years old.".format(sliced_name, age)

print("\nFull Name: ", full_name)
print("Sliced Name: ", sliced_name)
print("Greeting Message: ", greet)