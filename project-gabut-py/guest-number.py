import random

angka_maks = 10
angka_min = 2

while True:
    def guess():
        user_input = int(input('masukkan angka tebakkan: '))
        if user_input == random.randint(angka_min, angka_maks):
            print('YEAYY Congrats! this is Cookie for you🍪!')
        else:
            print('Do it Again, Dont Surrender bro🔁')
    guess()