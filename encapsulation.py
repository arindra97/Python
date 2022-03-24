# Definisikan class Karyawan
class Karyawan: 
    nama_perusahaan = 'ABC' 
    __insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.__nama = nama
        self.__usia = usia 
        self.__pendapatan = pendapatan 
        self.__pendapatan_tambahan = 0
    def lembur(self):
        self.__pendapatan_tambahan += self.__insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.__pendapatan_tambahan +=insentif_proyek 
    def total_pendapatan(self):
        return self.__pendapatan + self.__pendapatan_tambahan
# Buat objek karyawan bernama Aksara
aksara = Karyawan('Aksara', 25, 8500000)
# Akses ke attribute class Karyawan
print(aksara.__class__.nama_perusahaan)
# Akan menimbulkan error ketika di run
print(aksara.__nama)


# Inheritance
# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())
# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.tambahan_proyek(2000000)
print(senja.total_pendapatan())

#Modified Inheritance
# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
# Buat kembali class turunan (sebagai inherit class) dari class karyawan,  
# yaitu class IlmuwanData
class IlmuwanData(Karyawan):
    # mengubah atribut insentif_lembur yang digunakan pada fungsi lembur()
    insentif_lembur = 500000
    def __init__(self, nama, usia, pendapatan): 
        super().__init__(nama, usia, pendapatan)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())
# Buat objek karyawan yang bekerja sebagai IlmuwanData
senja = IlmuwanData('Senja', 28, 13000000)
senja.lembur()
print(senja.total_pendapatan())

# Polymorpishm
# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
    # menerapkan polymorphism dengan mendefinisikan kembali fungsi 
    # lembur() pada class AnalisData 
    def lembur(self):
        # pendapatan tambahan pada class AnalisData sebesar
        # 10 % dari pendapatannya.
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan): 
        super().__init__ (nama, usia, pendapatan)
    # mendefinisikan kembali fungsi lembur() pada class AnalisData 
    def lembur(self):
        # memanggil fungsi lembur pada class Karyawan 
        super().lembur()
        # pendapatan tambahan pada class AnalisData sebesar
        # 5 % dari pendapatannya.
        self.pendapatan_tambahan += int(self.pendapatan*0.05)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())

#Overloading
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    # usia akan di-set nilainya menjadi 21 saat tidak
    # dispesifikasikan dan pendapatan akan di-set nilainya
    # menjadi 5000000 saat tidak dispesifikasikan
    def __init__(self, nama, usia=21, pendapatan=5000000): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Karyawan baru pertama yang bernama Budi
karyawan_baru1 = Karyawan('Budi')
print(karyawan_baru1.nama)
print(karyawan_baru1.usia)
print(karyawan_baru1.total_pendapatan())
# Karyawan baru ke-2 yang bernama Didi, umur 25
karyawan_baru2 = Karyawan('Didi', 25)
print(karyawan_baru2.nama)
print(karyawan_baru2.usia)
print(karyawan_baru2.total_pendapatan())
# Karyawan baru ke-3 yang bernama Hadi, pendapatan 8000000
karyawan_baru3 = Karyawan('Hadi', pendapatan=8000000)
print(karyawan_baru3.nama)
print(karyawan_baru3.usia)
print(karyawan_baru3.total_pendapatan())