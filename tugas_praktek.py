#----Manipulation

'''
SOAL
Tugas Praktek
“Aksara, untuk praktik kali ini, saya membebaskan kamu memilih case yang akan digunakan,” ujar Senja padaku.

Aku pun mulai berpikir. Selama ini aku bikin program hitung-menghitung untuk kantor dan keluarga, kok enggak bikin buat diri sendiri juga yah? Apalagi belakangan aku suka nge-boba, kayaknya memang harus dilacak deh pengeluaran dan pemasukanku minimal 9 bulan terakhir. Kalau begitu, aku pakai case pengalamanku sendiri ini saja untuk dianalisis!

Buat menganalisisnya, berarti aku harus merapikan struktur data yang kumiliki terlebih dulu dengan dictionary dan kuberi nama keuangan untuk merepresentasikan pengeluaran dan pemasukan. “Pakai format juta, lalu masukkan variabel keuangan,” ujarku sembari mengetik


Tugas:
Dari variabel keuangan, aku akan menghitung rata-rata pengeluaran dan pemasukanku selama 9 bulan terakhir. Semoga keuanganku sehat-sehat saja. 
'''
# Data keuangan
keuangan = {
'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}
# Perhitungan rata-rata pemasukan dan rata-rata pengeluaran
total_pengeluaran = 0
total_pemasukan = 0
for biaya in keuangan['pengeluaran']: 
    total_pengeluaran += biaya
for biaya in keuangan['pemasukan']: 
    total_pemasukan += biaya
rata_rata_pengeluaran = total_pengeluaran / len(keuangan['pengeluaran']) 
rata_rata_pemasukan = total_pemasukan / len(keuangan['pemasukan'])
print(rata_rata_pengeluaran) 
print(rata_rata_pemasukan)


# Menghitung jumlah kemunculan kata
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
jumlah_artikel_jeruk = 0
jumlah_artikel_salak = 0
for judul in judul_artikel:
    if judul.count("Jeruk") > 0: 
        jumlah_artikel_jeruk += 1
    if judul.count("Salak") > 0:
        jumlah_artikel_salak += 1
print(jumlah_artikel_jeruk) 
print(jumlah_artikel_salak)

# Menghitung kata Positif
judul_artikel = [
"Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
"Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
"Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
"Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
"Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
"Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
"Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
"Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
"Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
"Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
kata_positif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kata_positif_jeruk = 0
kata_positif_salak = 0
for judul in judul_artikel: 
    for kata in kata_positif:
        if judul.count("Jeruk") > 0 and judul.count(kata) > 0: 
            kata_positif_jeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata) > 0:
            kata_positif_salak += 1
print(kata_positif_jeruk) 
print(kata_positif_salak)
