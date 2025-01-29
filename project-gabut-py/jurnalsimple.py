print("Welcome to SimpleJurnalApp.")
print("===========================")

while True:
    nama_jurnal = "jurnal.txt"
    pilianUser = input("\n1. Lihat Jurnal Kamu Kemarin\n2. Tulis Jurnal Kamu Hari Ini\n\nPilihan Kamu: ")

    def tulis():
        userTanggal = input("Masukkan Tanggal, (Contoh: 28 Desember 2024): ")
        userInput = input("Ketik perasaan mu hari ini, dan juga komentar mu: ")
        with open(nama_jurnal, "a") as file:
            file.write(f"pada tanggal {userTanggal}, isi jurnal kamu:\n-> {userInput}\n")

    def lihat():
        try:
            with open(nama_jurnal, "r") as file:
                jurnal = file.read()
                if jurnal:
                    print(jurnal)
                else:
                    print("\nJurnal Masih Kosong")
        except FileNotFoundError:
            print("\nFile Jurnal Tidak Ditemukan.")

    if pilianUser == "1":
        lihat()

    elif pilianUser == "2":
        tulis()

    else:
        print("Tidak ada di Menu.")

