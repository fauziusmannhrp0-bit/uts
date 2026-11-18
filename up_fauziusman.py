
print("======================================")
print("          SELAMAT DATANG")
print("======================================")

total_belanja = 0

while True:
    print("\n========== INPUT DATA MAKANAN ==========")

    nama_makanan = input("Nama makanan       : ")
    harga = int(input("Harga makanan      : Rp"))
    jumlah = int(input("Jumlah pembelian   : "))

    # Menghitung total harga setiap transaksi
    subtotal = harga * jumlah

    # Menambahkan subtotal ke total belanja
    total_belanja += subtotal

    print("--------------------------------------")
    print("Nama Makanan       :", nama_makanan)
    print("Subtotal           : Rp", format(subtotal, ",").replace(",", "."))
    print("--------------------------------------")

    # Menanyakan transaksi berikutnya
    pilihan = input("Tambah transaksi? (y/n): ").lower()

    if pilihan == "n":
        break

# Menghitung dan menentukan diskon
print("\n======================================")
print("             RINCIAN BELANJA")
print("======================================")

print("Total Belanja      : Rp", format(total_belanja, ",").replace(",", "."))

if total_belanja > 100000:
    diskon = total_belanja * 10 / 100
    print("Status Diskon      : Selamat! Anda mendapatkan diskon 10%.")
else:
    diskon = 0
    print("Status Diskon      : Maaf, Anda tidak mendapatkan diskon.")

# Menghitung total pembayaran
total_pembayaran = total_belanja - diskon

print("--------------------------------------")
print("Diskon             : Rp", format(int(diskon), ",").replace(",", "."))
print("Total Pembayaran   : Rp", format(int(total_pembayaran), ",").replace(",", "."))
print("======================================")
print("       TERIMA KASIH TELAH BERBELANJA!")
print("======================================")
