# Semua ini adalah nama variabel yang valid dan penugasan yang sah

user_name = "joanne"
user_id = 18
verified = True

# Nilai variabel dapat diubah setelah penugasan

points = 8
print(points)
points = 18
print(points)

# Fungsi print() digunakan untuk mencetak teks, angka, atau informasi lain yang dapat dicetak ke konsol.
print("Hello World!")

print(100)

pi = 3.14159
print(pi)

# Komentar pada satu baris

user = "Zakin"  # Komentar setelah kode

# Sebuah string adalah rangkaian karakter (huruf, angka, spasi, atau tanda baca) yang dikelilingi oleh tanda kutip.
# Ini dapat dikelilingi menggunakan tanda kutip ganda " atau tanda kutip tunggal '.
# Jika string harus dipecah menjadi beberapa baris, karakter backslash \ dapat digunakan
# untuk menunjukkan bahwa string tersebut berlanjut pada baris berikutnya.
user = "User Full Name"
game = "Monopoly"

longer = "This string is broken up \
over multiple lines"

print(longer)

# Penggabungan string di mana dua atau lebih string digabungkan menggunakan operator +.

first = "Hello "
second = "World"

result = first + second
print(result)
long_result = first + second + "!"
print(long_result)
# Contoh angka bulat

chairs = 4
tables = 1
broken_chairs = -2
sofas = 0

# Angka non-bulat atau Angka pecahan (Floating point)

lights = 2.5
left_overs = 0.0
pi = 3.14159
meal_cost = 12.99
tip_percent = 0.20

# Errors
# Interpreter Python akan melaporkan kesalahan yang ada dalam kode Anda.
# Untuk sebagian besar kasus kesalahan, interpreter akan menampilkan baris kode di mana
# kesalahan tersebut terdeteksi dan menempatkan karakter caret ^ di bawah bagian kode di mana kesalahan tersebut terdeteksi.

"""if False ISNOTEQUAL True:
                  ^
SyntaxError: invalid syntax
"""

# ZeroDivisionError
# ZeroDivisionError dilaporkan oleh interpreter Python ketika ia mendeteksi operasi pembagian sedang dilakukan dan penyebut (angka bawah) adalah 0.
# Dalam matematika, membagi sebuah angka dengan nol tidak memiliki nilai yang didefinisikan,
# sehingga Python menganggapnya sebagai kondisi kesalahan dan akan melaporkan ZeroDivisionError
# serta menampilkan baris kode di mana pembagian terjadi. Hal ini juga dapat terjadi jika sebuah variabel digunakan sebagai penyebut dan nilainya diatur menjadi atau diubah menjadi 0.

"""numerator = 100
denominator = 0
bad_results = numerator / denominator

ZeroDivisionError: division by zero
"""

# SyntaxError
# SyntaxError dilaporkan oleh interpreter Python ketika sebagian dari kode tidak benar.
# Ini bisa termasuk kata kunci yang salah eja, kurang atau terlalu banyak tanda kurung atau tanda kurung,
# operator yang salah, kurang atau terlalu banyak tanda kutip, atau kondisi lainnya.

"""
age = 7 + 5 = 4

File "<stdin>", line 1
SyntaxError: can't assign to operator
"""

# NameError
# NameError dilaporkan oleh interpreter Python ketika ia mendeteksi variabel yang tidak dikenal.
# Ini dapat terjadi ketika sebuah variabel digunakan sebelum nilainya diberikan
# atau jika nama variabel tersebut dieja secara berbeda dibandingkan dengan tempat di mana variabel tersebut didefinisikan.
# Interpreter Python akan menampilkan baris kode di mana NameError terdeteksi dan menunjukkan nama yang tidak didefinisikan tersebut.

"""
misspelled_variable_name

NameError: name 'misspelled_variable_name' is not defined
"""
