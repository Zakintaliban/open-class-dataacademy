# Input Pengguna dalam Python

# Fungsi input() digunakan untuk menerima input dari pengguna.
user_input = input("Masukkan sesuatu: ")

# Input yang diterima dari pengguna adalah string.
# Anda perlu mengonversinya ke tipe data lain jika diperlukan.
# Contoh: Konversi input pengguna ke integer
angka = int(input("Masukkan angka: "))

# Anda dapat memberikan pesan atau instruksi kepada pengguna
# untuk menjelaskan input yang diharapkan.
nama_pengguna = input("Masukkan nama Anda: ")

# Anda juga dapat menggunakan input() untuk mengambil beberapa input
# dan memisahkan mereka dengan spasi, kemudian memisahkan hasilnya menjadi list.
data = input("Masukkan beberapa angka (pisahkan dengan spasi): ").split()

# Anda dapat melakukan operasi dengan input yang diterima.
angka1 = 1
angka2 = 2
hasil_penjumlahan = angka1 + angka2

# Ingatlah untuk memeriksa dan menangani input yang tidak valid atau tipe data yang tidak diharapkan.
try:
    nilai = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
