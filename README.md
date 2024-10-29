# Program Pemesanan Tiket Bioskop dan Program Kalkulator Sederhana

**Kasus 1 : Program Pemesanan Tiket Bioskop**

**Flowchart**

![Screenshot_25](https://github.com/user-attachments/assets/aff79e50-3e2a-49a6-a404-023e04ceeaf5)

**Kode Python**

If Else

![Tiket Bioskop(If Elif Else)](https://github.com/user-attachments/assets/60e14c09-5ac3-4afa-bb68-dff4df52cd53)

Operator Ternary

![Tiket Bioskop(Operator Ternary)](https://github.com/user-attachments/assets/6ff7eda2-5a10-4cec-8b7f-b66c040a054f)

**Input dan Output**

![Output tiket bioskop](https://github.com/user-attachments/assets/b800fa28-88b8-4524-af2f-c75366e6ec4f)

**Penjelasan Program Python :**

**Variabel Awal**

- harga_reguler dan harga_vip menyimpan harga tiket reguler dan VIP.
- diskon_member adalah diskon sebesar 20% (0.2) yang akan diterapkan jika pengguna memiliki kartu member.

**Input dari User**

- input() digunakan untuk menerima data dari user.
- strip() digunakan untuk menghapus spasi yang tidak diperlukan di awal atau akhir input.
- lower() memastikan bahwa input berupa huruf kecil agar lebih mudah diperiksa (case-insensitive).

**Pemilihan Tipe Tiket dengan if-elif-else**

- Jika memilih "reguler", maka harga tiket diatur ke Rp50.000.
- Jika memilih "vip", harga tiket diatur ke Rp100.000.
- Jika input tipe tiket tidak valid (bukan "reguler" atau "vip"), program mencetak pesan error dan keluar dengan exit().

**Penghitungan Diskon untuk Member**

- Jika memiliki kartu member ("ya"), harga dikurangi sebesar 20% dengan rumus:
- total_harga = harga × (1−0.2)
- Jika tidak memiliki kartu member ("tidak"), total harga tetap sama.

**Output Total Harga**
- print() digunakan untuk menampilkan hasil total harga tiket kepada user.

**Kasus 2 : Program Kalkulator Sederhana**

**Flowchart**

![Screenshot_26](https://github.com/user-attachments/assets/1e346eb2-1fd2-486b-b81f-29a86c5683ce)

**Kode Python**

![Kode Python Operasi Matematika](https://github.com/user-attachments/assets/c627b4cf-7a9a-4806-bef5-85c5a2f9d9b7)

**Input dan Output**

![Operasi Matematika](https://github.com/user-attachments/assets/c0e4fb94-b158-4bc5-a8c4-657e37ebdf35)

**Pembagian dengan nol**

![Operasi pembagian 0](https://github.com/user-attachments/assets/7a983076-c7fb-4e00-86e1-df6627d54b88)

**Penjelasan Program Python :**

- Program meminta pengguna untuk memasukkan dua angka.
- Fungsi input() membaca data dari pengguna, dan float() mengubah input menjadi bilangan desimal (floating-point) agar bisa digunakan untuk operasi matematika.
- Selanjutnya, pengguna diminta memasukkan operator (+, -, *, atau /) sebagai string.

**Kondisi if-elif-else digunakan untuk memeriksa operator yang dipilih:**
- Jika operator adalah +, maka dua angka akan dijumlahkan.
- Jika operator adalah -, program melakukan pengurangan.
- Jika operator adalah *, program mengalikan dua angka.
- Jika operator adalah /, maka pembagian dilakukan jika angka kedua tidak nol.
- Jika angka kedua nol, muncul pesan kesalahan dan program berhenti menggunakan exit().
- else pada akhir memastikan bahwa program mendeteksi jika pengguna memasukkan operator tidak valid (bukan +, -, *, atau /).

**Pembagian dengan nol:**
Saat operator pembagian dipilih, program memeriksa apakah angka kedua adalah nol. Pembagian dengan nol tidak diperbolehkan karena akan menghasilkan error, jadi program menampilkan pesan "Error: Pembagian dengan nol tidak diperbolehkan." dan berhenti.

**Operator tidak valid:**
Jika pengguna memasukkan operator selain +, -, *, atau /, program akan menampilkan pesan "Operator tidak valid!" dan berhenti.


