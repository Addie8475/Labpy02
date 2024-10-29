# Harga tiket
harga_reguler = 50000
harga_vip = 100000
diskon_member = 0.2  # 20% diskon

# Input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

# Hitung harga tiket
if tipe_tiket == "reguler":
    harga = harga_reguler
elif tipe_tiket == "vip":
    harga = harga_vip
else:
    print("Tipe tiket tidak valid!")
    exit()

# Terapkan diskon jika memiliki kartu member
if member == "ya":
    total_harga = harga * (1 - diskon_member)
else:
    total_harga = harga

# Output hasil
print(f"Total harga yang harus dibayar: Rp{total_harga}")
