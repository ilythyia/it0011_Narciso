def sum_of_digits(input_string):
    total = 0
    
    for char in input_string:
        if char.isdigit():
            total += int(char)
    
    print(f"Sum of digits: {total}")

user_input = input("Enter a string containing digits: ")
sum_of_digits(user_input)