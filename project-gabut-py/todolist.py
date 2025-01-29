import json

nama_file = "my_activity.json"

def ambil_data():
    try:
        with open(nama_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def simpan_data(data):
    with open(nama_file, "w") as file:
        json.dump(data, file, indent=1)

kegiatan = ambil_data()

print('\nSelamat Datang di To-Do-List 📝')
print('=============================')
while True:
    print('\n1. Lihat Kegiatan Saat Ini\n2. Tambah Kegiatan\n3. Hapus Kegiatan\n4. Keluar\n')
    input_user = int(input('Masukkan Pilihan Anda (Hanya Angka): '))
    print()

    def tambah_kegiatan():
        tambah = input('masukkan kegiatan yang ingin ditambah: ')
        if ', ' and ' ' in tambah:
            pisah = tambah.split(', ')
            for i in pisah:
                kegiatan.append(i)
        else:
            kegiatan.append(tambah)
        simpan_data(kegiatan)

    def hapus_kegiatan():
        hapus = input('masukkan kegiatan yang ingin dihapus: ')
        if hapus in kegiatan:
            if ', ' in hapus:
                pisah = hapus.split(', ')
                for i in pisah:
                    if i in kegiatan:
                        kegiatan.remove(i)
            else:
                kegiatan.remove(hapus)
            simpan_data(kegiatan)
        else:
            print(f"\n'{hapus}' tidak ada di dalam daftar")
        

    def lihat_kegiatan():
        print("Daftar Kegiatan Daat ini: ")
        if kegiatan:
            for idx, item in enumerate(kegiatan, 1):
                print(f"{idx}. {item}")
        else:
            print("Tidak ada Kegiatan Saat Ini. ")

    if input_user <= 4:
        if input_user == 1:
            lihat_kegiatan()
        elif input_user == 2:
            tambah_kegiatan()
        elif input_user == 3:
            hapus_kegiatan()
        elif input_user == 4:
            print('Terimakasih telah menggunakan!')
            break
        else:
            print('Input Harus 1-4.')