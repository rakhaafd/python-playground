from functools import reduce 

a = [1,2,3]
n = reduce(lambda x,y : x + (x*y), a)
print(n)

# Langkah 1: x = 1, y = 2 → 1 + (1 * 2) = 3
# Langkah 2: x = 3 (dari iterasi pertama), y = 3 → 3 + (3 * 3) = 12