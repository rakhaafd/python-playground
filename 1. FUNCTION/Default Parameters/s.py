# jika kita mempunyai 3 parameter def func(a,b,c), maka semuanya harus memiliki default variable atau:

# parameter c memiliki default variable dan parameter a & b tidak,
# parameter c dan b memiliki default variable dan parameter a tidak.
# namun apabila parameter a dan c memiliki default variable dan b tidak, maka akan terjadi error.

def print_star(n = '1'):
  for i in range(n):
    print("*****************************")

print_star(3)