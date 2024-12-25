# urutan argumen yang kita teruskan ke dalam function akan sama ketika diterima oleh function

# Saat memanggil function, daripada hanya meneruskan nilai argumen, kita dapat meneruskan argumen dengan menentukan nama argumen yang disebut sebagai keyword parameters.

# Berikut contoh penggunaan keyword parameters
def get_root(a,b,c):
  r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return r1,r2

result1, result2 = get_root(a=1,c=-8,b=2) # sama saja dengan (1, 2, -8)
print('Hasil akar-akarnya adalah', result1, 'atau', result2)

#output
# Hasil akar-akarnya adalah 2.0 atau -4.0