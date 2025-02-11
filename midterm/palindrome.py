def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        for i, line in enumerate(lines, start=1):
            numbers = list(map(int, line.strip().split(',')))
            total_sum = sum(numbers)
            result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
            print(f"Line {i}: {line.strip()} (sum {total_sum}) - {result}")
            
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError:
        print("Error: The file contains invalid data.")

process_file("numbers.txt") 
