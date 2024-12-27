import multiprocessing
import time

# Mendeklarasikan fungsi yang akan dijalankan dalam proses terpisah
def print_numbers(n):
    for i in range(n):
        time.sleep(1)  # Simulasi proses dengan delay 1 detik
        print(f"Nomor: {i+1}")

# Membuat proses dan menjalankan fungsi dengan parameter
p1 = multiprocessing.Process(target=print_numbers, args=(5,))  # Argumen 5 akan dikirimkan ke print_numbers
p1.start()  # Memulai proses

# Menunggu proses p1 selesai sebelum melanjutkan ke baris berikutnya
p1.join()

print("Proses selesai!")