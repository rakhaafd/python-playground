# program threading sederhana
import threading
import time

# Mendeklarasikan fungsi yang akan dijalankan dalam thread
def print_numbers(n):
    for i in range(n):
        time.sleep(0.1)  # Simulasi proses dengan delay 1 detik
        print(f"Nomor: {i+1}")

# Membuat thread dan menjalankan fungsi dengan parameter
t1 = threading.Thread(target=print_numbers, args=(100,))  # Argumen 5 akan dikirimkan ke print_numbers
t1.start()  # Memulai thread

# Menunggu thread t1 selesai sebelum melanjutkan ke baris berikutnya
t1.join()

print("Thread selesai!")