# FOR

# fungsi yang dapat melakukan perulangan pada setiap jenis variabel berupa kumpulan atau urutan.
for huruf in "Dicoding":  # Contoh pertama
    print("Huruf: {}".format(huruf))

flowers = ["mawar", "melati", "anggrek"]
for flower in flowers:  # Contoh kedua
    print("Flower: {}".format(flower))

# WHILE
# blok statement yang mengikuti kondisi while dan memiliki posisi indentasi yang sama,
# dianggap blok statement yang akan dieksekusi.
count = 0
while count < 7:
    print("Hitungannya adalah: {}".format(count))
    count = count + 1

var = 1
while var == 1:  # This constructs an infinite loop
    num = input("Masukkan angka: ")
    print("Anda memasukkan angka: {}".format(num))

while True:  # This constructs an infinite loop
    num = input("Masukkan angka: ")
    print("Anda memasukkan angka: {}".format(num))

def do_something(): 
    print("something")

# while one line
while (True): do_something()

for i in range(0, 6):
    for j in range(0, 6 - i):
        print('*', end='')
    print()

# output
# ******
# *****
# ****
# ***
# **
# *