userI = int(input('masukkan angka untuk difaktorial: '))
def factorial (n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

fac = factorial(userI)
print(fac)