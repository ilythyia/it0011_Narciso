def pattern_b():
    i = 1
    while i <= 7:
        if i % 2 == 1 or i == 6:
            print(" " * (7 - i) + str(i) * i)
        i += 1
        
print("\nPattern B:")
pattern_b()