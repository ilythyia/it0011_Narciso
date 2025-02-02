def pattern_a():
    for i in range(1, 6):
        print(" " * (6 - i) + "".join(str(num) for num in range(1, i + 1)))
        
print("Pattern A:")
pattern_a()