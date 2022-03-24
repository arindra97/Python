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



# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan  
# Definisikan class Perusahaan
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat 
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)

class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan 

# Definisikan perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021)95205xx')
# Definisikan nama-nama karyawan
karyawan_1 = Karyawan('Ani', 25, 8500000, 100000)
karyawan_2 = Karyawan('Budi', 28, 12000000, 150000)
karyawan_3 = Karyawan('Cici', 30, 15000000, 200000)
# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan_1) 
perusahaan.aktifkan_karyawan(karyawan_2) 
perusahaan.aktifkan_karyawan(karyawan_3)


# Encapsulation, Inheritance, Polymorphism
# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += nilai_proyek * 0.01
# Definisikan class AnalisData sebagai child class dari
# class Karyawan
class AnalisData(Karyawan): 
	pass
# Definisikan class IlmuwanData sebagai child class dari
# class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += 0.1 * nilai_proyek
# Definisikan class PembersihData sebagai child class dari
# class TenagaLepas
class PembersihData(TenagaLepas): 
    pass
# Definisikan class DokumenterTeknis sebagai child class dari
# class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def tambahan_proyek(self, jumlah_tambahan): 
        return


# Definisikan class Karyawan sebagai parent class
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur 
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self,jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class TenagaLepas sebagai child class dari class Karyawan 
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan, 0)
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += nilai_proyek * 0.01

# Definisikan class AnalisData sebagai child class dari class Karyawan 
class AnalisData(Karyawan):
    def __init__(self, nama, usia = 21, pendapatan = 6500000, 
                 insentif_lembur = 100000):
        super().__init__(nama, usia, pendapatan, insentif_lembur) 

# Definisikan class IlmuwanData sebagai child class dari class Karyawan
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia = 25, pendapatan = 12000000, 
                 insentif_lembur = 150000):
        super().__init__(nama, usia, pendapatan, insentif_lembur) 
    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += 0.1 * nilai_proyek 

# Definisikan class PembersihData sebagai child class dari class TenagaLepas
class PembersihData(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 4000000): 
        super().__init__(nama, usia, pendapatan)

# Definisikan class DokumenterTeknis sebagai child class dari class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def __init__(self, nama, usia, pendapatan = 2500000): 
        super().__init__(nama, usia, pendapatan)

# Definisikan class Perusahaan 
class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon): 
        self.nama = nama
        self.alamat = alamat 
        self.nomor_telepon = nomor_telepon 
        self.list_karyawan = []
    def aktifkan_karyawan(self, karyawan): 
        self.list_karyawan.append(karyawan)
    def nonaktifkan_karyawan(self, nama_karyawan): 
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                karyawan_nonaktif = karyawan 
                break
        if karyawan_nonaktif is not None: 
            self.list_karyawan.remove(karyawan_nonaktif)
    def total_pengeluaran(self): 
        pengeluaran = 0
        for karyawan in self.list_karyawan:
            pengeluaran += karyawan.total_pendapatan() 
        return pengeluaran
    def cari_karyawan(self, nama_karyawan): 
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan: 
                return karyawan
        return None

# Create object karyawan sesuai dengan tugasnya masing-masing
# seperti yang dinyatakan dalam tabel.
ani = PembersihData('Ani',25)
budi = DokumenterTeknis('Budi',18)
cici = IlmuwanData('Cici')
didi = IlmuwanData('Didi',32,20000000)
efi = AnalisData('Efi')
febi = AnalisData('Febi',28,12000000)

# Create object perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11','(021)95812xx')

# Aktifkan setiap karyawan yang telah didefinisikan
perusahaan.aktifkan_karyawan(ani)
perusahaan.aktifkan_karyawan(budi)
perusahaan.aktifkan_karyawan(cici)
perusahaan.aktifkan_karyawan(didi)
perusahaan.aktifkan_karyawan(efi)
perusahaan.aktifkan_karyawan(febi)

# Cetak keseluruhan total pengeluaran perusahaan
print(perusahaan.total_pengeluaran())