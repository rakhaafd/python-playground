import pywhatkit as kit

# Nomor tujuan (format internasional)
nomor = "+62895339023888"
pesan = "Halo, ini adalah pesan otomatis dari Python!"

# Mengirim pesan langsung tanpa menunggu
kit.sendwhatmsg_instantly(nomor, pesan, wait_time=10)  # Tunggu 10 detik sebelum mengirim