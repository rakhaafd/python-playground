def closure_calc():
    a = 2
    def mult(x):
        return a * x
    return mult

c = closure_calc()  # Mengembalikan fungsi mult, tetapi belum dijalankan
print(c(1))  # Baru di sini fungsi mult dijalankan, dengan x=1