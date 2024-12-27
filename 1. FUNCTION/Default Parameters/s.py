# jika kita mempunyai 3 parameter def func(a,b,c), maka semuanya harus memiliki default variable atau:

# parameter c memiliki default variable dan parameter a & b tidak,
# parameter c dan b memiliki default variable dan parameter a tidak.
# namun apabila parameter a dan c memiliki default variable dan b tidak, maka akan terjadi error.

def print_star(n = 2):
  for i in range(n):
    print("*****************************")

print_star(4)

def add_numbers(a, b=0, c=0):
    return a + b + c

print(add_numbers(5))  # Output: 5
print(add_numbers(5, 10))  # Output: 15
print(add_numbers(5, 10, 15))  # Output: 30