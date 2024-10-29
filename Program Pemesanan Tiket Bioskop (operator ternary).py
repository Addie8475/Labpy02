# Harga tiket
harga_reguler = 50000
harga_vip = 100000
diskon_member = 0.2  # 20%

# Meminta input dari pengguna
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

# Menentukan harga awal dengan ternary operator
harga_awal = harga_reguler if tipe_tiket == "reguler" else harga_vip if tipe_tiket == "vip" else None

# Validasi tipe tiket
if harga_awal is None:
    print("Tipe tiket tidak valid.")
    exit()

# Menghitung total harga dengan ternary operator
total_harga = harga_awal * (1 - diskon_member) if member == "ya" else harga_awal

# Menampilkan total harga
print(f"Total harga yang harus dibayar: Rp{total_harga:,}")
