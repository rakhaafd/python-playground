# soal 1 - menampilkan angka ganjil
numbers = [10, 15, 21, 34, 47, 52, 63, 78, 91]

for i in filter(lambda x: x % 2 == 1, numbers):
    print(i)

# soal 2 - Mengubah nama menjadi huruf kapital
names = ['rakha', 'fausta', 'adinata', 'raharja']

capital = list(map(lambda n: n.capitalize(), names)) #map() digunakan untuk menerapkan fungsi lambda ke setiap elemen dalam daftar names.

print(capital)

# soal 3 - Perkalian elemen dalam list
numbers = [2, 4, 6, 8, 10]

operation = list(map(lambda n: n * 2, numbers))
print(operation)

# soal 4 - Menghitung panjang kata
words = ['banana', 'apple', 'cherry', 'blueberry', 'kiwi']

sortir = list(map(lambda n: len(n), words))
print(sortir)

# soal 5 - Memfilter angka positif
numbers = [-10, 20, -30, 40, -50, 60]

for i in filter(lambda n: n >= 0, numbers):
    print(i)

# soal 6 - Menghitung kuadrat angka
numbers = [1, 3, 5, 7, 9]
kuadrat = list(map(lambda n: n ** 2, numbers))
print(kuadrat)

# soal 7 - Memfilter kata yang mengandung huruf "a"
words = ['cat', 'dog', 'elephant', 'tiger', 'antelope']

for i in filter(lambda n: 'a' in n, words):
    print(i)