def count_characters(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    space_count = 0
    other_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            space_count += 1
        else:
            other_count += 1
    
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Spaces: {space_count}")
    print(f"Other Characters: {other_count}")

user_input = input("Enter a string: ")
count_characters(user_input)
