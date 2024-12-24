userI1 = int(input('masukkan angka pertama .. '))
userI2 = int(input('masukkan angka kedua .. '))

def operation (n1, n2):
    return n1 + n2 # mengembalikan hasil menggunakan return

result = operation(userI1, userI2)
print(result)

def get_root (a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2

res1, res2 = get_root(a=1, c=-8, b=2)
print(res1, res2)