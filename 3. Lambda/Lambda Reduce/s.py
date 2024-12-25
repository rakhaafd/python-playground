# versi menggunakan map
# a = [1, 2, 3, 4]
# n = list(map(lambda x: x ** 2, a))
# print(n)

# reduce version (ciri ciri reduce:

# Fungsi diterapkan pada dua elemen pertama, lalu hasilnya diterapkan dengan elemen berikutnya, dan seterusnya, hingga seluruh elemen diiterasi.)

from functools import *

def sum (a, b):
    operasi = input('masukkan operasi.. +\n-\n*\n/\n\n')
    if operasi == '+':
        return a + b

    elif operasi == '-':
        return a - b

    elif operasi == '*':
        return a * b

    elif operasi == '/':
        return a / b
    
i = list(map(int, input('masukkan angka yang ingin anda sum, pisah dg spasi .. ').split()))

result = reduce(sum, i)
print(result)