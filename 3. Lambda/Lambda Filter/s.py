umur = [18, 24, 35, 42, 23]
print('umur yang dewasa')
for a in filter(lambda x: x >= 18, umur):
    print(a, end=' ')

# Lambda function di atas mengembalikan True untuk x sama dengan atau lebih dari 19 dan menggunakan filter(), kita bisa menyaring dan hanya mencetak nilai usia yang sama dengan atau lebih dari 19.