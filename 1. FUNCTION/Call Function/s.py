# memanggil function
userInput = 'rakha'
def ini_func(sapaaku):
    print('haii, salam kenal! ', sapaaku)
    return sapaaku

ini_func(userInput)


rows = int(input('masukkan berapa kali generate bintang .. '))

def generate_rows(x):
    for i in range (x):
        print(' ' * (x - i - 1), end='')
        # Cetak bintang untuk setiap baris
        print('*' * (2 * i + 1))

generate_rows(rows)