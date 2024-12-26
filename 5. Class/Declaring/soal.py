# soal: membuat program hewan peliharaan
class Pet:
    def speak(self, nama, jenis, suara):
        print(nama, 'adalah seekor', jenis, 'dan bersuara:', suara)

hewan = Pet()

hewan.speak('andika', 'anjing', 'awooo')

#soal: program kendaraan
class Vehicle:
    def vehicle_action(self, jenis, merk, warna):
        # Menampilkan informasi kendaraan
        print(f"Kendaraan ini adalah sebuah {jenis} dengan merk {merk} dan warna {warna}")
        # Menampilkan kendaraan sedang berjalan
        print(f"Kendaraan {merk} sedang berjalan")

# Membuat dua instance dari Vehicle
ins1 = Vehicle()
ins2 = Vehicle()

# Memanggil method untuk instance pertama
ins1.vehicle_action('sepeda motor', 'honda', 'merah')

# Memanggil method untuk instance kedua
ins2.vehicle_action('mobil', 'toyota', 'hitam')