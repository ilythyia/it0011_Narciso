def count_unique_words(statement):
    exclusions = {
        "and", "but", "or", "nor", "for", "so", "yet",
        "a", "an", "the",
        "of"
    }
    
    words = statement.split()
    
    word_count = {}
    
    for word in words:
        clean_word = ''.join(char for char in word if char.isalnum())
        
        if clean_word.lower() not in exclusions and clean_word:
            if clean_word in word_count:
                word_count[clean_word] += 1
            else:
                word_count[clean_word] = 1
    
    lower_case_words = {word: count for word, count in word_count.items() if word.islower()}
    upper_case_words = {word: count for word, count in word_count.items() if word.isupper()}
    
    sorted_lower_case = sorted(lower_case_words.items())
    sorted_upper_case = sorted(upper_case_words.items())
    
    sorted_unique_words = sorted_lower_case + sorted_upper_case
    
    total_words_filtered = sum(lower_case_words.values()) + sum(upper_case_words.values())
    
    for word, count in sorted_unique_words:
        print(f"{word:<10} - {count}")
    
    print(f"Total words filtered: {total_words_filtered}")

if __name__ == "__main__":
    statement = input("Enter a string statement:\n")
    count_unique_words(statement)