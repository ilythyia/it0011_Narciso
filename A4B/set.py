 # Defining sets
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# a. Number of elements in A and B
A_B_union = A | B
print("Number of elements in A and B:", len(A_B_union))

# b. Elements in B that are not in A and C
B_only = B - (A | C)
print("\nElements in B that are not in A and C:", B_only)

# c. Show the required sets using set operations
set1 = C - A  # [h, i, j, k]
print("\n[h, i, j, k]:  ", set1)

set2 = C & A  # [c, d, f]
print("[c, d, f]:  ", set2)

set3 = B & (A | C)  # [b, c, h]
print("[b, c, h]:  ", set3)

set4 = (A & C) - B  # [d, f]
print("[d, f]:  ", set4)

set5 = A & B & C  # [c]
print("[c]:  ", set5)

set6 = B - (A | C)  # [l, m, o]
print("[l, m, o]:  ", set6)
