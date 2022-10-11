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
