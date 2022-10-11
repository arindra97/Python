kata = 'diCoDing'
kata = kata.upper()
print(kata)
kata = kata.lower()
print(kata)

# menghapus whitespace pada sebelah kanan string atau akhir string
print('Dicoding    '.rstrip())
# menghapus whitespace pada sebelah kiri atau awal string.
print('    Dicoding'.lstrip())
# menghapus whitespace pada bagian awal atau akhir string.
print('    Dicoding    '.strip())
# menghilangkan kata tertentu
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip('Code'))

# mengembalikan nilai True jika string diawali dengan kata awalan tertentu
print('Dicoding Indonesia'.startswith('Dicoding'))
# mengembalikan nilai True jika string diakhiri dengan kata akhiran tertentu
print('Dicoding Indonesia'.endswith('Indonesia'))

# join
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('-'.join(['Dicoding', 'Indonesia', '!']))
# split
print('Dicoding Indonesia !'.split())
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# Replace (case sensitive)
string = "Ayo belajar Coding di Dicoding. karena Coding xxxxx"
print(string.replace("Coding", "Pemrograman"))
# Opsional: Parameter ketiga pada replace dapat diisi jumlah substring yang ingin diganti
print(string.replace("Coding", "Pemrograman", 1))

# Pengecekan String
kata = "DICODING"
kata.isupper()
kata.islower()
kata.isalpha()  # mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet
kata.isalnum()  # mengembalikan nilai True jika karakter dalam string adalah alfanumerik
# mengembalikan nilai True jika karakter dalam string berisi hanya angka/numerik,
'1234'.isdecimal()
# isspace()
# istitle()

# contoh penggunaan untuk validasi
while True:
    print('Masukkan nama Anda:')
    name = input()
    if name.isalpha():
        print("Halo", name)
        break
    print('Masukkan nama Anda dengan benar.')

# Formatting pada String
# data di konversi ke string terlebih dahulu karena format aslinya int
# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print(str(angka).zfill(5))
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print(str(angka).zfill(5))
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
# hasil sama karena jumlah karakter yang ada sudah berjumlah 5 yang di mana karakter koma (“,”) dan negatif (“-”) juga dihitung
print(str(angka).zfill(5))
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(7))

# tidak perlu ubah string karena sudah bertipe string
# Contoh 1
kata = 'aku'
print(kata.zfill(5))
# Contoh 2
kata = 'kamu'
print(kata.zfill(5))
# Contoh 3
kata = 'dirinya'
print(kata.zfill(5))

# Teks rata kanan/kiri/tengah dengan rjust(), ljust(), dan center()
'Dicoding'.rjust(20)
'Dicoding'.ljust(20)
'Dicoding'.ljust(20, '!')
'Dicoding'.center(20)

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# Memberikan nilai untuk multiple variable
data = ['shirt', 'white', 'L']  # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data

a = 6
b = 4
print("Hasilnya " + str(a + b) + "6" * 3)
