'''
1. Arithmetic operators

+   | Penambahan         | 3 + 2 akan menghasilkan output: 5 
-   | Pengurangan        | 4 - 2 akan menghasilkan output: 2
*   | Perkalian          | 3 * 2 akan menghasilkan output: 6 
/   | Pembagian          | 3 / 2 akan menghasilkan output: 1.5      
%   | Modulo/sisa bagi   | 3 % 2 akan menghasilkan output: 1 dikarenakan 3 tidak habis dibagi 2 dan menyisakan 1, 8 % 2 akan menghasilkan output: 0 dikarenakan 8 habis dibagi 2
**  | Pangkat            |3 ** 2 akan menghasilkan output: 9
//  | Pembagian dengan pembulatan ke bawah|3 // 2 akan menghasilkan output: 1|dikarenakan 1.5 akan menjadi 1 saat dibulatkan ke bawah.

2. Assignment operators
+=

Penambahan

x = 3

x += 2 ekivalen dengan x = x + 2

akan mengubah nilai x menjadi 5

-=

Pengurangan

x = 3

x -= 2 ekivalen dengan x = x - 2

akan mengubah nilai x menjadi 1

*=

Perkalian

x = 3

x *= 2 ekivalen dengan x = x * 2

akan mengubah nilai x menjadi 6

/=

Pembagian

x = 3

x /= 2 ekivalen dengan x = x / 2

akan mengubah nilai x menjadi 1.5

%=

Modulo/sisa bagi

x = 3

x %= 2 ekivalen dengan x = x % 2

akan mengubah nilai x menjadi 1

**=

Pangkat

x = 3

x **= 2 ekivalen dengan x = x ** 2

akan mengubah nilai x menjadi 9

//=

Pembagian dengan pembulatan ke bawah

x = 3

x //= 2 sama dengan x = x // 2

akan mengubah nilai x menjadi 1

3. Comparison operators
==

Persamaan

33 == 33 akan menghasilkan output: True dikarenakan benar 33 sama dengan 33

34 == 33 akan menghasilkan output: False dikarenakan 34 tidak sama dengan 33

!=

Pertidaksamaan

34 != 33 akan menghasilkan output: True dikarenakan benar bahwa 34 tidak sama dengan 33

33 != 33 akan menghasilkan output: False dikarenakan 33 sama dengan 33

> 

Lebih besar dari

34 > 33 akan menghasilkan output: True dikarenakan 34 lebih besar dari 33

33 > 34 akan menghasilkan output False dikarenakan tidak benar 33 lebih besar dari 34

< 

Lebih kecil dari

33 < 34 akan menghasilkan output True dikarenakan benar 33 lebih kecil dari 34

34 < 33 akan menghasilkan output: False dikarenakan tidak benar 34 lebih kecil dari 33

>=

Lebih besar atau sama dengan

34 >= 33 akan menghasilkan output True dikarenakan 34 lebih besar dari 33

34 >= 34 akan menghasilkan output True dikarenakan 34 sama dengan 34

33 >= 34 akan menghasilkan output False dikarenakan 33 tidak lebih besar dari 34 dan tidak sama dengan 34

<=

Lebih kecil atau sama dengan

33 <= 34 akan menghasilkan output True dikarenakan 33 lebih kecil dari 34

33 <= 33 akan menghasilkan output True dikarenakan 34 sama dengan 33

34 <= 33 akan menghasilkan output False dikarenakan 34 tidak lebih kecil dari 33 dan tidak sama dengan 34

4. Logical operators

and

dan - menerima dua nilai kebenaran dan mengembalikan nilai benar jika keduanya benar

x = 5

x >= 1 and x <= 10

akan mengembalikan nilai True

x = 5

x >= 1 and x <= 4

akan mengembalikan nilai False

or

atau - menerima dua nilai kebenaran dan mengembalikan nilai benar jika salah satu benar

x = 3

x >= 1 or x <= 2

akan mengembalikan nilai True dikarenakan statemen logika pertama terpenuhi

x = 3

x >= 5 or x <= 0

akan mengembalikan nilai False dikarenakan kedua statemen logika tidak terpenuhi (bernilai False)

not

negasi - menerima sebuah nilai kebenaran dan mengembalikan komplemennya

x = 7

not(x == 7) akan mengembalikan nilai False

not(x >= 10) akan mengembalikan nilai True

5. Identity operators
is

Menerima dua buah objek dan mengembalikan nilai True ketika keduanya merujuk pada objek yang sama dan False dalam kondisi lainnya

x = ["Ani", "Budi"]

y = ["Ani", "Budi"]

a = x

print(a is x) akan menampilkan nilai True dikarenakan a dan x merujuk ke objek yang sama

print(a is y) akan menampilkan nilai False dikarenakan a dan y tidak merujuk ke objek yang sama meskipun isi di dalam keduanya sama.

is not

Menerima dua buah objek dan mengembalikan nilai True ketika keduanya merujuk pada objek yang berbeda dan False jika sama

x = ["Ani", "Budi"]

y = ["Ani", "Budi"]

a = x

print(a is not x) akan menampilkan nilai False dikarenakan a dan x merujuk ke objek yang sama

print(a is not y) akan menampilkan nilai   True dikarenakan a dan y tidak merujuk ke objek yang sama

6. Membership operators
in

Menerima sebuah sequence/set dan objek, mengembalikan True ketika objek merupakan anggota dari sequence/set, dan False ketika bukan.

x = ["Ani", "Budi", "Cici"]

y = "Cici"

z = "Dodi"

print(y in x) akan menampilkan nilai   True

print(z in x) akan menampilkan nilai  False

not in

Menerima sebuah sequence/set dan objek, mengembalikan True ketika objek bukan merupakan anggota dari sequence/set, dan False ketika merupakan.

x = ["Ani", "Budi", "Cici"]

y = "Cici"

z = "Dodi"

print(y not in x) akan menampilkan nilai  False

print(z not in x) akan menampilkan nilai   True
'''


#Nilai Prioritas Operator dalam Python
# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga # baris pertama
harga_bayar *= total_harga # baris kedua
pajak_bayar = pajak * harga_bayar # baris ketiga
harga_bayar += pajak_bayar # baris ke-4
print("Kode awal - harga_bayar=", harga_bayar)
# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga #baris pertama 
harga_bayar += harga_bayar * pajak # baris kedua
print("Penyederhanaan kode - harga_bayar=", harga_bayar)

'''
()

10

Kiri ke kanan

Grouping

x[index]

9

Kiri ke kanan

Mengakses elemen array

**

8

Kanan ke kiri

pangkat

+x

-x

7

Kiri ke kanan

Tanda bilangan positif dan negatif

*

/

%

6

Kiri ke kanan

Perkalian Pembagian Modulus

+

-

5

Kiri ke kanan

Penambahan Pengurangan

is, is not, in, not in

<=, <, >=, >

==, !=

4

Kiri ke kanan

Membership operator Comparison Operator

not

3

Kiri ke kanan

Operator logika negasi (not)

and

2

Kiri ke kanan

Operator logika konjungsi (and)

or

1

Kiri ke kanan

Operator logika disjungsi (or)
'''