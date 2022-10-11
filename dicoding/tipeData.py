# integer, float, complex
a = 10
print(a, "bertipe", type(a))
b = 1.7
print(b, "bertipe", type(b))
c = 1+2j
print(c, "Bertipe bilangan kompleks?", isinstance(1+2j, complex))

# Integer tidak dibatasi oleh angka atau panjang tertentu
x = [0]*10005  # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1] = 1  # x[1]=1

for j in range(2, 10001):
    x[j] = x[j-1]+x[j-2]  # Fibonacci
print(x[10000])

# string
s = "Ini adalah string baris tunggal"
s = '''Ini adalah string
yang memiliki baris pertama
dan selanjutnya baris kedua'''

# List
a = [1, 2.2, 'python']

x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])
# x[0] artinya mengambil elemen paling awal, dengan index 0 dari List x.
# x[5] artinya mengambil elemen dengan index 5 dari List x.
# x[-1] artinya mengambil elemen dengan index paling belakang ke-1 dari List x.
# x[3:5] artinya membuat list dari anggota elemen List x dengan index 3 hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 3-4).
# x[:5] artinya membuat list dari anggota elemen List x paling awal hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 0-4).
# x[-3:] artinya membuat list dari anggota elemen List x mulai index ke-3 dari belakang hingga paling belakang.
# x[1:7:2] artinya membuat list dari anggota elemen List x dengan index 1 hingga sebelum index 7, dengan "step" 2 (dalam hal ini hanya index 1, 3, 5).

# Elemen pada list dapat diubah atau ditambahkan.
x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

# Untuk menghapus item pada list, gunakan fungsi del.
binatang = ['kucing', 'rusa', 'badak', 'gajah']
del binatang[2]
print(binatang)

# Slicing pada String
s = "Hello World!"
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
# ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
s = "Halo Dunia!"
print(s)

# Tuple
t = (5, 'program', 1+3j)
print(t[1])
print(t[0:3])
# print(t[0]=10)  # error

# Set
a = {1, 2, 2, 3, 3, 3}
print(a)

# Dictionary
d = {1: 'value', 'key': 2}
print(type(d))
print("d[1] = ", d[1])
print("d['key'] = ", d['key'])
