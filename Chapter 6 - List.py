# contoh list
primes = [2, 3, 5, 7, 11]
print(primes)

empty_list = []

# menggabungkan 2 list
items = ["cake", "cookie", "bread"]
total_items = items + ["biscuit", "tart"]
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# method append atau nambah
orders = ["daisies", "periwinkle"]
orders.append("tulips")
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']

# indexing(?)

names = ["Roger", "Rafael", "Andy", "Novak"]
print(names[2])  # siapa?

soups = ["minestrone", "lentil", "pho", "laksa"]
# To select the last element, my_list[-1]:
# Untuk memilih elemen terakhir dalam daftar my_list, gunakan indeks -1.
# Ini akan mengembalikan elemen terakhir dari daftar.

# To select the last three elements, my_list[-3:].
# Untuk memilih tiga elemen terakhir dalam daftar my_list, gunakan slicing dengan indeks -3:.
# Ini akan mengembalikan tiga elemen terakhir dari daftar.

# To select everything except the last two elements, my_list[:-2].
# Untuk memilih semua elemen kecuali dua elemen terakhir dalam daftar my_list, gunakan slicing dengan :-2.
# Ini akan mengembalikan semua elemen dalam daftar kecuali dua elemen terakhirnya.

soups[-1]  # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil'
