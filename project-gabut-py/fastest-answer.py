import random
import time

operator = ["+", "-", "*", "/"]
angka_minimal = 2
angka_maksimal = 10
jumlah_soal = 10

def buat_soal():
    while True:
        angka_kanan = random.randint(angka_minimal, angka_maksimal)
        angka_kiri = random.randint(angka_minimal, angka_maksimal)
        operasi = random.choice(operator)

        #pastikan tidak ada pembagian 0
        if operasi == "/" and angka_kanan == 0:
            continue

        ekspresi = f"{str(angka_kiri)} {operasi} {str(angka_kanan)}"
        jawaban = eval(ekspresi)

        #pastikan jwbn bilangan bulat bulat
        if isinstance(jawaban, int):
            return ekspresi, jawaban

salah = 0
input("🎯 Tekan ENTER Untuk Memulai .. ")
print("====================================")

waktu_mulai = time.time()
for i in range(jumlah_soal):
    ekspresi, jawaban = buat_soal()
    while True:
        input_user = input(f"Soal ke-{str(i + 1)} : {ekspresi} = ")
        if input_user == str(jawaban):
            print("Benar!\n")
            break
        else:
            print("Coba lagi!\n")
        salah += 1

waktu_akhir = time.time()
total_waktu = waktu_akhir - waktu_mulai

print("====================================")
print(f"Kerja bagus💪, Kamu selesai dalam waktu {total_waktu} detik!")